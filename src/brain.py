import config
import requests

def ask_gideon(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": config.model_Name,
        "prompt": prompt,
        "system": config.system_prompt,
        "stream": config.stream
    }

    response = requests.post(url, json=payload)
    data = response.json()
    return data["response"]