from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
from my_tools.hotel_tools import add_hotel, get_hotel_info, list_hotels


hotel_agent = Agent(
    name="Hotel Assistant",
    instructions=(
        "You are a helpful hotel assistant. "
        "You can add hotels, list all hotels, and provide information about them. "
        "Always use the tools to manage hotel details."
    ),
    tools=[add_hotel, get_hotel_info, list_hotels],
    model=GEMINI_MODEL
)
