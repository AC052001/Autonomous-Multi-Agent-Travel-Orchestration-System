from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.refiner_agent.agent import refiner_agent
from .sub_agents.idea_agent.agent import idea_agent
from .sub_agents.memory_agent.agent import memory_agent
from .tools.weather_agent.agent import get_weather
from .tools.flight_agent.agent import get_flight_status
from .tools.hotel_agent.agent import hotel_agent


MODEL = "gemini-2.5-flash"


# --- Root Agent (Coordinator) ---
root_agent = LlmAgent(
    model=MODEL,
    name="manager_agent",
    description="Coordinates specialist agents to provide final travel plans.",
    instruction="""
    You are the lead planner coordinating the Smart Travel system.
    1. Collect user request and context.
    2. Use MemoryAgent to recall past preferences.
    3. Call IdeaAgent to propose options.
    4. Call RefinerAgent to ensure they fit within budget and preferences.
    5. Combine results into a single travel plan using all the tools.
    """,
    sub_agents=[refiner_agent, memory_agent],
    tools=[
        AgentTool(idea_agent),
        get_weather,
        get_flight_status,
        hotel_agent
    ]
)
