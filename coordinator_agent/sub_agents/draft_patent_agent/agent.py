"""Draft Patent Agent for generating patent drafts."""

from google.adk.agents import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-flash"

draft_patent_agent = Agent(
    model=MODEL,
    name="draft_patent_agent",
    instruction=prompt.DRAFT_PATENT_PROMPT,
    tools=[google_search],
    output_key="draft_patent",
)