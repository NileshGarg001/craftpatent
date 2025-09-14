from google.adk.agents import LoopAgent, Agent
from google.adk.tools import google_search

from coordinator_agent.prompts import DRAFT_PATENT_PROMPT, RATE_PATENT_PROMPT

MODEL = "gemini-2.5-flash"

# Draft Patent Agent
draft_patent_agent = Agent(
    model=MODEL,
    name="draft_patent_agent",
    instruction=DRAFT_PATENT_PROMPT,
    tools=[google_search],
    output_key="current_draft",
)

# Rate Patent Agent  
rate_patent_agent = Agent(
    model=MODEL,
    name="rate_patent_agent",
    instruction=RATE_PATENT_PROMPT,
    output_key="current_rating",
    tools=[google_search],
)


# Coordinator LoopAgent
coordinator_agent = LoopAgent(
    name="coordinator_agent",
    description="A coordinator agent that manages the iterative patent creation process.",
    max_iterations=3,
    sub_agents=[
        draft_patent_agent,
        rate_patent_agent
    ],
)

root_agent = coordinator_agent
