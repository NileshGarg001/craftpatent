from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

from .prompt import COORDINATOR_AGENT_INSTRUCTION
from .sub_agents.draft_patent_agent import draft_patent_agent
from .sub_agents.rate_patent_agent import rate_patent_agent

MODEL = "gemini-2.5-flash"

coordinator_agent = LlmAgent(
    name="coordinator_agent",
    model=MODEL,
    description="A coordinator agent that manages the patent creation process.",
    instruction=COORDINATOR_AGENT_INSTRUCTION,
    output_key="final_patent",
    tools=[
        AgentTool(agent=draft_patent_agent),
        AgentTool(agent=rate_patent_agent),
    ],
)

root_agent = coordinator_agent
