from tools import get_time, get_weather, calculator
available_tools = {
    "get_weather": get_weather,
    "calculator": calculator,
    "get_time": get_time
}
def execute_tool(tool_name, **arguments):
    tool_function = available_tools.get(tool_name)
    if tool_function is None:
        raise Exception(f"Tool function '{tool_name}' not found.")
    return tool_function(**arguments)