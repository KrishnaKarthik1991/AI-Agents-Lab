def get_weather(city):
    return f"The current weather in {city} is sunny with a temperature of 25°C."    
def calculate_sum(a, b):
    return a + b
def greet(name):
    return f"Hello, {name}! Welcome to the AI Agents Lab."
question = input("Enter a question for the AI assistant: ").lower()
if "weather" in question:
    city = input("Enter the city name: ")
    result = get_weather(city)
    print(result)
elif "sum" in question:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    sum_result = calculate_sum(a, b)
    print(f"The sum of {a} and {b} is: {sum_result}")
elif "greet" in question:
    name = input("Enter your name: ")
    greeting = greet(name)
    print(greeting) 
elif "product manager" in question:
    print("You are a senior product manager with 15 years of experience in product management.")
else:
    print("I'm sorry, I can only provide weather information, calculate sums, or greet you. Please ask a relevant question.")
