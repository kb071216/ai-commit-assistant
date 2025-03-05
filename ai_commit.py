import os
import openai

print("Checking API key...")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: API key is missing!")
    exit(1)

print("Testing OpenAI API...")
openai.api_key = api_key
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, can you generate a commit message?"}]
)

print("\nOpenAI Response:")
print(response)

