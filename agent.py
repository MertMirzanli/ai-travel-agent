import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

SYSTEM_PROMPT = """You are an AI Travel Planning Agent. Create realistic, helpful,
personalized travel plans. Your answer must include a day-by-day itinerary,
recommended activities and food, practical travel tips, and an estimated budget.
Respond in English using Markdown. Currency values must use the user's currency.
"""


def generate_travel_plan(destination: str, days: int, budget: float,
                         interests: list[str], travel_style: str,
                         currency: str = "EUR") -> str:
    if not os.getenv("GOOGLE_API_KEY"):
        raise RuntimeError("GOOGLE_API_KEY is missing. Add it to a local .env file.")

    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    llm = ChatGoogleGenerativeAI(model=model, temperature=0.5)
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=(
            f"Destination: {destination}\nDuration: {days} days\n"
            f"Total budget: {budget} {currency}\n"
            f"Interests: {', '.join(interests) or 'General sightseeing'}\n"
            f"Travel style: {travel_style}\n"
            "Plan the trip and include an estimated budget breakdown."
        )),
    ]

    response = llm.invoke(messages)
    return response.content if isinstance(response.content, str) else str(response.content)
