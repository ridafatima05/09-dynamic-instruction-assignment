from agents import function_tool, RunContextWrapper
from typing import Dict

# --- Context ---
class HotelContext:
    def __init__(self):
        # Store multiple hotels
        self.hotels: Dict[str, str] = {}

# --- Tools ---
@function_tool
def add_hotel(ctx: RunContextWrapper[HotelContext], name: str, info: str) -> str:
    """
    Add a new hotel with some info (location, rooms, amenities, etc.).
    """
    ctx.context.hotels[name.lower()] = info
    return f"✅ Hotel '{name}' added."

@function_tool
def get_hotel_info(ctx: RunContextWrapper[HotelContext], name: str) -> str:
    """
    Retrieve details of a hotel by name.
    """
    hotel = ctx.context.hotels.get(name.lower())
    if hotel:
        return f"🏨 {name}: {hotel}"
    return f"❌ No info found for hotel '{name}'."

@function_tool
def list_hotels(ctx: RunContextWrapper[HotelContext]) -> str:
    """
    List all stored hotels.
    """
    if not ctx.context.hotels:
        return "⚠️ No hotels added yet."
    return "📋 Hotels: " + ", ".join(ctx.context.hotels.keys())
