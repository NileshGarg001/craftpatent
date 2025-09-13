from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool


from .prompt import RATING_AGENT_INSTRUCTION

MODEL = "gemini-2.5-flash"

coordinator_agent = LlmAgent(
    name="rating_agent",
    model=MODEL,
    description="An agent that rates the quality and grantability of a patent application.",
    instruction=RATING_AGENT_INSTRUCTION,
)

root_agent = coordinator_agent
