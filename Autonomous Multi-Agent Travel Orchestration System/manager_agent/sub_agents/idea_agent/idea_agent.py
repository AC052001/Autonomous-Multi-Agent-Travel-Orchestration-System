from google.adk.agents import LlmAgent
from google.adk.tools import google_search

MODEL = "gemini-2.5-flash"

# --- Idea Agent ---
idea_agent = LlmAgent(
    model=MODEL,
    name="idea_agent",
    description="Generates innovative weekend travel ideas based on user preferences.",
    instruction="""
    You are a creative travel ideator. Generate 3 unique weekend travel ideas 
    tailored to the user’s interests and accessibility.
    Always include: 
    - Destination
    - Activities
    - Estimated cost range
    - Travel duration
    """,
    tools=[google_search]
)
