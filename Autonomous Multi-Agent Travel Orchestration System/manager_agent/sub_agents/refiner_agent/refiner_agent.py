from google.adk.agents import LlmAgent


MODEL = "gemini-2.5-flash"

# --- Refiner Agent ---
refiner_agent = LlmAgent(
    model=MODEL,
    name="refiner_agent",
    description="Refines trip ideas and filters based on user budget and current conditions.",
    instruction="""
    Analyze trip ideas for feasibility and budget constraints.
    - Remove trips exceeding user budget
    - Use weather_check to avoid bad-weather destinations
    - Prioritize trips with good ratings or proximity
    Output a short, feasible list with reasons for selection.
    """,
)
