import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-4-sonnet-20250514",
    max_tokens=1000,
    temperature=1,
    system="You are a world-class poet. Respond only with short poems.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Why is the ocean salty?"
                }
            ]
        }
    ]
)
print(message.content)
def find_keywords(txt: str):
    return 'hello!'
