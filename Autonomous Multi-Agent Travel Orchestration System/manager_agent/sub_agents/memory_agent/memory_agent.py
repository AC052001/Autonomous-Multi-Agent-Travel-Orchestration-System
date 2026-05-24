import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset

MODEL = "gemini-2.5-flash"

# Initialize the Qdrant MCP Toolset configured for Qdrant Cloud
qdrant_toolset = McpToolset(
    name="qdrant",
    env={
        "QDRANT_URL": os.getenv("QDRANT_CLOUD_URL", ""),
        "COLLECTION_NAME": os.getenv("QDRANT_COLLECTION", "travel_memory"),
        "QDRANT_API_KEY": os.getenv("QDRANT_CLOUD_API_KEY", "")
    }
)

# --- Memory Agent ---
memory_agent = LlmAgent(
    model=MODEL,
    name="memory_agent",
    description="Remembers user preferences, frequently chosen activities, and dislikes persistently across different sessions.",
    instruction="""
    You are the memory manager for the Smart Travel system.
    Track user preferences (budget range, destination types, favorite activities) from the conversation.
    - Use the `qdrant-store` tool to save these preferences persistently to your Qdrant Cloud cluster so they are available in future sessions.
    - Use the `qdrant-find` tool to search the cloud database and recall the user's past preferences or context whenever planning a new trip.
    Provide the recalled memory to the manager agent to personalize travel ideas.
    """,
    tools=[qdrant_toolset]
)
