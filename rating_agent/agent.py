from google.adk.agents import LlmAgent
from .prompt import RATING_AGENT_INSTRUCTION

root_agent = LlmAgent(
    name="rating_agent",
    model="gemini-2.5-flash",
    description="An agent that rates the quality and grantability of a patent application.",
    instruction=RATING_AGENT_INSTRUCTION,
)