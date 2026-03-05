from dotenv import load_dotenv
from google.adk.agents import Agent
from src.agents.query_agent import query_agent
from src.prompts.query_prompt import ROOT_AGENT_INSTRUCTION, SAMPLE_PROMPT_INSTRUCTION

load_dotenv() 

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    instruction=ROOT_AGENT_INSTRUCTION,
    sub_agents=[query_agent]
)