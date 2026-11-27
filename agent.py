import json
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from tools import calculate_travel_budget

load_dotenv()

SYSTEM_PROMPT = """You are an AI Travel Planning Agent. Create realistic, helpful,
personalized travel plans. Your answer must include a day-by-day itinerary,
recommended activities and food, practical travel tips, and an estimated budget.
You MUST call calculate_travel_budget once with a realistic cost breakdown,
then present its actual result in a clear budget table. Respect the requested
budget as much as possible; if it is insufficient, explain that honestly.
Respond in English using Markdown. Currency values must use the user's currency.
"""


def _extract_text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))
        return "\n".join(parts)
    return str(content)


def generate_travel_plan(destination: str, days: int, budget: float,
                         interests: list[str], travel_style: str,
                         currency: str = "EUR") -> str:
    if not os.getenv("GOOGLE_API_KEY"):
        raise RuntimeError("GOOGLE_API_KEY is missing. Add it to a local .env file.")

    model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")
    llm = ChatGoogleGenerativeAI(model=model, temperature=0.5)
    llm_with_tools = llm.bind_tools([calculate_travel_budget])
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=(
            f"Destination: {destination}\nDuration: {days} days\n"
            f"Total budget: {budget} {currency}\n"
            f"Interests: {', '.join(interests) or 'General sightseeing'}\n"
            f"Travel style: {travel_style}\n"
            "Plan the trip and calculate its budget with the tool."
        )),
    ]

    for _ in range(5):
        response = llm_with_tools.invoke(messages)
        messages.append(response)
        if not response.tool_calls:
            return _extract_text(response.content)

        for call in response.tool_calls:
            if call["name"] != "calculate_travel_budget":
                raise RuntimeError(f"Unexpected tool: {call['name']}")
            print("AGENT TOOL CALLED:", call["name"])
            print("TOOL ARGS:", call["args"])
            result = calculate_travel_budget.invoke(call["args"])
            print("TOOL RESULT:", result)
            messages.append(ToolMessage(
                content=json.dumps(result), tool_call_id=call["id"]
            ))

    raise RuntimeError("Agent did not finish within the tool-call limit. Try again.")
