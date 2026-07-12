import config
import requests
from memory import conversation



def ask_gideon(conversation):
    prompt = ""

    for message in conversation:
        prompt += f"{message['role']}: {message['content']}\n"

    print(prompt)

    url = config.OLLAMA_URL

    payload = {
        "model": config.MODEL_NAME,
        "prompt": prompt,
        "system": config.SYSTEM_PROMPT,
        "stream": config.STREAM
    }


    response = requests.post(url, json=payload)
    print(response.status_code)
    print(response.text)

    data = response.json()
    return data["response"]