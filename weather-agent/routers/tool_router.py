from tools.weather import get_weather
from tools.calculator import calculator
from tools.time_tool import get_time
from tools.joke import get_joke
available_tools = {
    "get_weather": get_weather,
    "calculator": calculator,
    "get_time": get_time,
    "get_joke": get_joke
}
def execute_tool(tool_name, **arguments):
    tool_function = available_tools.get(tool_name)
    if tool_function is None:
        raise Exception(f"Tool function '{tool_name}' not found.")
    return tool_function(**arguments)  