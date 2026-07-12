import requests
import json

def ask_gideon(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3.1",
        "prompt": prompt,
        "system": "You are Gideon, an advanced AI assistant. Respond in maximum 2 short sentences only. Be concise, intelligent and direct. No bullet points. No long explanations. Address the user as Zohaib.",
        "stream": False
    }

    response = requests.post(url, json=payload)
    data = response.json()
    return data["response"]

print("Gideon online. How may I assist you?")

while True:
    user_input = input("You:")
    if user_input.lower() == "exit":
        print("Gideon: Goodbye, Zohaib.")
        break
    response = ask_gideon(user_input)
    print(f"Gideon: {response}")