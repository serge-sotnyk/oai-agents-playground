import os

from agents import Agent, Runner
from dotenv import load_dotenv
# import litellm

# Load environment variables from .env file
load_dotenv()
# litellm._turn_on_debug()

model = os.getenv("MINIMAL_TEST_MODEL")

agent = Agent(model=model, name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)
