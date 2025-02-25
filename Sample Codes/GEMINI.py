from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.google import Gemini
from dotenv import load_dotenv
import os
from agno.utils.pprint import pprint_run_response 


# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Using Google AI Studio
agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp", api_key=api_key,),
    markdown=True
)



# Print the response in the terminal
try:
   response_stream: Iterator[RunResponse] = agent.run("Explain AI to me in simple terms.", stream=True) 
except Exception as e:
    print(f"Error occurred: {type(e).__name__}: {str(e)}")

pprint_run_response(response_stream, markdown=True)
