from agno.agent import Agent, RunResponse
from agno.models.huggingface import HuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("HUGGINGFACE_API_KEY")
if not api_key:
    raise ValueError("HUGGINGFACE_API_KEY not found in .env file")

agent = Agent(
    model=HuggingFace(
        id="meta-llama/Meta-Llama-3-8B-Instruct",
        max_tokens=4096,
        api_key=api_key,
    ),
    markdown=True
)

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story.")