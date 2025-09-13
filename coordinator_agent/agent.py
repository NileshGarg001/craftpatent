from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool


from .prompt import RATING_AGENT_INSTRUCTION
from .sub_agents.academic_newresearch import academic_newresearch_agent
from .sub_agents.academic_websearch import academic_websearch_agent

MODEL = "gemini-2.5-flash"

coordinator_agent = LlmAgent(
    name="rating_agent",
    model=MODEL,
    description="An agent that rates the quality and grantability of a patent application.",
    instruction=RATING_AGENT_INSTRUCTION,
    tools=[google_search]
)

root_agent = coordinator_agent
