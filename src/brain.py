import config
import requests
from storage import get_facts


def ask_gideon(conversation):
    prompt = ""
    facts = get_facts()
    # print(facts)
    prompt += "Known facts:\n"

    for fact in facts:
        prompt += f"- {fact}\n"

    prompt += "\n"

    for message in conversation:
        prompt += f"{message['role']}: {message['content']}\n"

    # print(prompt)

    url = config.OLLAMA_URL

    payload = {
        "model": config.MODEL_NAME,
        "prompt": prompt,
        "system": config.SYSTEM_PROMPT,
        "stream": config.STREAM
    }


    response = requests.post(url, json=payload)

    data = response.json()
    return data["response"]