import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"
# prompt = "I Love You Baby!"
prompt = "Suggest a name for my clothing company."

message_system = {
    "role": "system",
    # "content": "You are my loving girlfriend"
    # "content": "You are my strict office colleague, who is also my manager"
    "content": "You are a brand manager who suggests name for my company. Name should be a one word name."
}

message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]

# temperature by default is 0, meaning safe
response = client.chat.completions.create(model=model, messages=messages, temperature=1)
# print(response)

# print("#########################")

answer = response.choices[0].message.content
print(answer)