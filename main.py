from agent import root_agent
from src.config.settings import load_config

load_config()  # loads .env

if __name__ == "__main__":
    # Run via ADK, FastAPI, or CLI depending on your setup
    root_agent.run()