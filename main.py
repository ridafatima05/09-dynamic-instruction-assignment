from agents import Runner, set_tracing_disabled
from my_agents.my_agents import hotel_agent
from my_tools.hotel_tools import HotelContext   # import context

set_tracing_disabled(True)

# Create context manually since Agent() doesn’t take context_type
context = HotelContext()

# Run the agent with context
result = Runner.run_sync(
    starting_agent=hotel_agent,
    input="Add Hotel Pearl in Karachi with 50 rooms and a spa.",
    context=context,
)

print(result.final_output)
