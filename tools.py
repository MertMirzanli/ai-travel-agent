from langchain_core.tools import tool


@tool
def calculate_travel_budget(
    accommodation: float,
    food: float,
    transport: float,
    attractions: float,
    other: float,
    total_budget: float,
) -> dict:
    """Calculate a trip's estimated total cost and remaining budget in the user's currency."""
    costs = {
        "accommodation": accommodation,
        "food": food,
        "transport": transport,
        "attractions": attractions,
        "other": other,
    }
    if any(value < 0 for value in costs.values()) or total_budget < 0:
        return {"error": "Budget and costs must be non-negative."}
    estimated_total = round(sum(costs.values()), 2)
    remaining = round(total_budget - estimated_total, 2)
    return {
        "breakdown": costs,
        "estimated_total": estimated_total,
        "total_budget": total_budget,
        "remaining_budget": remaining,
        "within_budget": remaining >= 0,
    }
