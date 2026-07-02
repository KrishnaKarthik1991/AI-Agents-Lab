from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.responses.create(
    model="gpt-5.5",
    input="Say hello to krishna and welcome him to AI Engineering."
)
print(response.output_text)
