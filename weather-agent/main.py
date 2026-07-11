from tools import get_weather
from openai import OpenAI
from dotenv import load_dotenv
import os

import requests

load_dotenv()
client = OpenAI()
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather for a given city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city to get the weather for."
                }
            },
            "required": ["city"]
        }
    }
]
user_question = input("Enter a question for the AI assistant: ")
response = client.responses.create(
    model="gpt-5.5",
    input=user_question,
    tools=tools,
)
print(response)
print("------------------------------")
print(response.output)
tool_call = response.output[0]
print(tool_call.name)
print(tool_call.arguments)
import json
arguments = json.loads(tool_call.arguments)
city = arguments["city"]
result = get_weather(city)
print(type(result))
print("Weather result")
print(result)
tool_call_id = tool_call.call_id
response2 = client.responses.create(
    model="gpt-5.5",
    previous_response_id=response.id,
    input=[
        {
            "type": "function_call_output",
            "call_id": tool_call_id,
            "output": result
        }
    ]
)
print(response2.output_text)
while True :
    user_question = input("Enter a question for the AI assistant: ")
    response = client.responses.create(
        model="gpt-5.5",
        input=user_question,
        tools=tools,
    )
    print(response)
    print("------------------------------")
    print(response.output)
    tool_call = response.output[0]
    print(tool_call.name)
    print(tool_call.arguments)
    import json
    arguments = json.loads(tool_call.arguments)
    city = arguments["city"]
    result = get_weather(city)
    print(type(result))
    print("Weather result")
    print(result)
    tool_call_id = tool_call.call_id
    response2 = client.responses.create(
        model="gpt-5.5",
        previous_response_id=response.id,
        input=[
            {
                "type": "function_call_output",
                "call_id": tool_call_id,
                "output": result
            }
        ]
    )
    print(response2.output_text)
    if user_question.lower() in ["exit", "quit"]:
        break
    