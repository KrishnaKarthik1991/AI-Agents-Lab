from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI()
def ask_llm(question, tools):
    response = client.responses.create(
        model="gpt-5.5",
        input=question,
        tools=tools,
    )
    return response
def send_tool_result(previous_response_id, tool_call_id, result):
    response2 = client.responses.create(
        model="gpt-5.5",
        previous_response_id=previous_response_id,
        input=[
            {
                "type": "function_call_output",
                "call_id": tool_call_id,
                "output": result
            }
        ]
    )
    return response2
