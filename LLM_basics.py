# pip install openai tiktoken
import tiktoken
# TOKENS - count cost
enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hello Sneha, welcome to Abu Dhabi"
tokens = enc.encode(text)
print(f"Tokens: {len(tokens)} -> {tokens}") # cost calculation
# TEMPERATURE & STREAMING with Ollama (local, free)
# First run: ollama run llama3.2:3b
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
response = client.chat.completions.create(
    model="llama3.2:3b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant for banking."}, # SYSTEM PROMPT
        {"role": "user", "content": "What is 2+2?"}
    ],
    temperature=0.2, # Low temp = factual
    stream=True # STREAMING
)
for chunk in response:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
print()


# for chunk in response:
#     print(chunk.choices[0].delta.content, end="", flush=True)