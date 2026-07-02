from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
conversation_history = []

while True:
    question = input("Welcome to Krishna's AI Assistant: ")
    conversation_history.append(
        {"role": "user", "content": question})
    if question.lower() == "exit":
        print("Goodbye!")
        break
    if question.lower() == " ":
        print("Please enter a valid question.")
        continue
    if question.lower() == "who am i":
        print("You are Krishna, a user of this AI assistant.")
        continue

    response = client.responses.create(
        model="gpt-5.5",
        input=conversation_history
    )
    answer = response.output_text
    conversation_history.append({"role": "assistant", "content": answer})

    print("AI:", answer)