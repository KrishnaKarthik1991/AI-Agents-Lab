from xmlrpc import client
from tools import calculator
from tools import get_weather
from openai import OpenAI
from dotenv import load_dotenv
from tool_router import execute_tool
import os
load_dotenv()
client = OpenAI()
import requests
from llm_router import ask_llm, send_tool_result
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
    },
    {
        "type": "function",
        "name": "calculator",
        "description": "Calculate the result of a mathematical expression.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to calculate."
                }
            },
            "required": ["expression"]
        }
    },
    {
        "type": "function",
        "name": "get_time",
        "description": "Get the current time.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]
user_question = input("Enter a question for the AI assistant: ")
response = ask_llm(user_question, tools)
print(response)
print("------------------------------")
print(response.output)
tool_call = None
for item in response.output:
    if item.type == "function_call":
        tool_call = item
        break
if tool_call is None:
    print(response.output_text)
    exit()
print(tool_call.name)
print(tool_call.arguments)
import json
arguments = json.loads(tool_call.arguments)
from tool_router import execute_tool
result = execute_tool(tool_call.name,**arguments)
response2 = send_tool_result(
    response.id,
    tool_call.call_id,
    result
)
print("======= RESPONSE 2 =======")
print(response2)
print("--------------------")
print(response2.output)
print("-------------------------")
print(response2.output_text)
print(type(result))
print("Tool result")
print(result)
tool_call_id = tool_call.call_id 
while True :
    user_question = input("Enter a question for the AI assistant: ")
    if user_question.lower() in ["exit", "quit"]:
        print("Exiting the program.")
        break
    if tool_call is None:
        print(response.output_text)
        continue
    response = ask_llm(user_question, tools)
    print(response)
    print("------------------------------")
    print(response.output)
    tool_call = None
    for item in response.output:
        if item.type == "function_call":
            tool_call = item
            break
    if tool_call is None:
        print(response.output_text)
        continue
    print(tool_call.name)
    print(tool_call.arguments)
    import json
    arguments = json.loads(tool_call.arguments)
    try:
        result = execute_tool(tool_call.name,**arguments)
    except Exception as e:
        result = f"Tool Error: {str(e)}"
    print(type(result))
    print("Tool result")
    print(result)
    tool_call_id = tool_call.call_id
    response2 = send_tool_result(
        response.id,
        tool_call_id,
        result
    )
    print(response2.output_text)
    model="gpt-5.5",
    previous_response_id=response.id,
    input=[
            {
                "type": "function_call_output",
                "call_id": tool_call_id,
                "output": result
            }
        ]
    print(response2.output_text)