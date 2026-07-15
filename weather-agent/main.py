import json

from routers.llm_router import ask_llm,send_tool_result
from routers.tool_router import execute_tool
from tool_schema import tools

def process_question(question):
    response = ask_llm(question, tools)

    tool_call = None

    for item in response.output:
        if item.type == "function_call":
            tool_call = item
            break

    if tool_call is None:
        return response.output_text

    arguments = json.loads(tool_call.arguments)

    result = execute_tool(tool_call.name, **arguments)

    response2 = send_tool_result(
        response.id,
        tool_call.call_id,
        result
    )

    return response2.output_text

while True:

    question = input("Ask: ")

    if question.lower() in ["exit", "quit"]:
        break

    answer = process_question(question)

    print(answer)