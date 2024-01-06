# import os
# from dotenv import load_dotenv

# import openai
# # import langchain # Not needed if you're not using anything directly from langchain
# # import langchain # This line is not needed if you're not using anything directly from langchain
# from langchain_community.llms import OpenAI

# load_dotenv()

# my_key = os.getenv("OPENAI_API_KEY")

# llm = OpenAI(temperature=0, model_kwargs={"open_api_key": my_key})
# text = ["what is AI?"]
# response = llm.generate(text)
# print(response)

import os
from dotenv import load_dotenv
from langchain_community.llms import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI from langchain_community with default temperature
# The API key is read from environment variables
llm = OpenAI(temperature=0)

# Define the text prompt
text = ["what is AI?"]

# Generate response using the llm object
response = llm.generate(text)

# Print the response
print(response)
