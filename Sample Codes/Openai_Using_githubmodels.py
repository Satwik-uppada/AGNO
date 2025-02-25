import os
from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response
from dotenv import load_dotenv

load_dotenv()

# Step 1: Retrieve the API key from an environment variable
OPENAI_API_KEY = os.getenv("GITHUB_TOKEN")
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API Key is missing! Please set it in the environment variables.")

# Step 2: Initialize the OpenAIChat model with your API key and model parameters
# (For educational purposes, GitHub might refer you to specific endpoints/models)
model = OpenAIChat(api_key=OPENAI_API_KEY, id="gpt-4o", temperature=0.7, base_url="https://models.inference.ai.azure.com")

# Step 3: Create an agent and use the model
agent = Agent(model=model)

# Query the agent for responses
# response: RunResponse = agent.run("Tell me a 5-second story about a robot!")
response_stream: Iterator[RunResponse] = agent.run("Explain AI to me in simple terms.", stream=True)

# # Step 4: Pretty-print responses with markdown format
# print("\nSingle response (short story):")
# pprint_run_response(response, markdown=True)

print("\nStreamed response (educational explanation):")
pprint_run_response(response_stream, markdown=True)
