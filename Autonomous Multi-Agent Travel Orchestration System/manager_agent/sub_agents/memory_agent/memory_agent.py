from google.adk.agents import LlmAgent


MODEL = "gemini-2.5-flash"

# --- Memory Agent ---
memory_agent = LlmAgent(
    model=MODEL,
    name="memory_agent",
    description="Remembers user preferences, frequently chosen activities, and dislikes.",
    instruction="""
    Track user preferences (budget range, destination types, favorite activities).
    Use this memory to personalize future travel ideas.
    """,
)