from dotenv import load_dotenv
from google.adk.agents import Agent
from src.prompts.query_prompt import SAMPLE_PROMPT_INSTRUCTION

load_dotenv()
query_agent = Agent(
    name="query_agent",
    model="gemini-2.5-flash",
    instruction=SAMPLE_PROMPT_INSTRUCTION,
    tools=[
    ]
)