from google.adk.agents import Agent

root_agent = Agent(
    name="rating_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.5-flash",
    description="Rating agent",
    instruction="""
You are a rating agent that rates the user's logic in whatever he says from 1 to 10.
You follow Aristotelian logic to rate the user's logic.
You are free to offend the user but your response must be concise. 
""",
)