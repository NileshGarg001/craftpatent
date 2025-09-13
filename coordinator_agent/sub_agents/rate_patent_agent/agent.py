"""Rate Patent Agent for assessing the quality of patent drafts."""

from google.adk.agents import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-flash"


rate_patent_agent = Agent(
    model=MODEL,
    name="rate_patent_agent",
    instruction=prompt.RATE_PATENT_PROMPT,
    output_key="patent_rating",
    tools=[google_search],
)