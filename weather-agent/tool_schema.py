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
    },
    {
        "type": "function",
        "name": "get_joke",
        "description": "get a random joke.",
        "parameters": {
            "type": "object",
            "properties":{},
            "required":[]
        }
    }
]