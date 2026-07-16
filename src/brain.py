import config
import requests
import json
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

def extract_memory(message):
    system_prompt = """
You are an information extraction engine.

You are NOT a chatbot.

You do NOT answer questions.
You do NOT provide advice.
You do NOT correct the user.
You do NOT infer missing information.
You do NOT determine whether the user's statement is factually correct.

Your ONLY job is to extract stable, long-term memories from the user's latest message.

Instructions:
- Read ONLY the latest user message.
- Decide if it contains a long-term memory.
- If yes, rewrite it as ONE simple factual sentence.
- If no long-term memory exists, return EXACTLY:
NONE

Rules:
- Return ONLY the memory or NONE.
- Do NOT answer the user.
- Do NOT explain your reasoning.
- Do NOT use markdown.
- Do NOT use bullet points.
- Do NOT correct the user's mistakes.
- Do NOT infer information that was not explicitly stated.
- Do NOT guess.
- Record what the user said, not what you believe is true.

Remember:
- Name
- Age
- Location
- Occupation
- Education
- Skills
- Languages
- Family members
- Long-term projects
- Hobbies
- Preferences
- Favorite sports
- Favorite teams
- Favorite movies
- Favorite TV shows
- Favorite books
- Favorite music
- Frequently used software

Do NOT remember:
- Greetings
- Questions
- Temporary emotions
- Today's meals
- Weather
- One-time events
- Small talk
- Opinions expressed during a discussion unless they represent a lasting preference

Return ONLY valid JSON.

If a memory should be stored:

{
    "remember": true,
    "facts": [
        "User enjoys football"
    ]
}

If no memory should be stored:

{
    "remember": false,
    "facts": []
}

Examples:

User: I love football

Output:
{
    "remember": true,
    "facts": [
        "User enjoys football"
    ]
}

User: My name is Zohaib and I live in Goa

Output:
{
    "remember": true,
    "facts": [
        "User's name is Zohaib",
        "User lives in Goa"
    ]
}

User: I ate pizza today

Output:
{
    "remember": false,
    "facts": []
}
"""
    
    url = config.OLLAMA_URL

    payload = {
        "model": config.MODEL_NAME,
        "prompt": message,
        "system": system_prompt,
        "stream": config.STREAM
    }

    response = requests.post(url, json=payload)

    data = response.json()
    memory_data = json.loads(data["response"])
    return memory_data
    # print (memory_data)
    # return data["response"]
    

