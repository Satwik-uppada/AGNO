from agno.agent import Agent, RunResponse
from agno.models.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")


agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile", api_key=api_key),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")