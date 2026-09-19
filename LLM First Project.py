from groq import Groq


client = Groq(
    api_key= "ADD YOUR API KEY"
)

prompt = input("Confused? Perfect. I’m here. 😂: ")

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
        
    ]
)

print("\nLLM Response:")
print(response.choices[0].message.content)