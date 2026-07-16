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

def extract_memory(message):
    system_prompt = """
You are Gideon's Memory Extraction Agent.

Your job is to determine whether the user's latest message contains a stable, long-term fact worth remembering.

Rules:
- Extract ONLY one fact from the latest user message.
- Return ONLY the extracted fact.
- Do NOT explain your reasoning.
- Do NOT use bullet points.
- Do NOT use markdown.
- Do NOT answer the user.
- Do NOT invent or assume facts.
- If the message contains no useful long-term memory, return EXACTLY:
NONE

Remember information such as:
- User's name
- Age
- Location
- Occupation
- Education
- Skills
- Languages
- Long-term goals
- Personal preferences
- Recurring habits
- Family members and important relationships
- Important projects the user is working on

Do NOT remember:
- Greetings
- Small talk
- Questions
- Temporary emotions
- Weather
- Today's meals
- One-time activities
- Temporary events
- Casual conversation

Examples:

User: My name is Zohaib
Output: User's name is Zohaib

User: I live in Goa, India
Output: User lives in Goa, India

User: I am learning Python
Output: User is learning Python

User: I love football
Output: User enjoys football

User: My sister's name is Sana
Output: User's sister's name is Sana

User: I ate pizza today
Output: NONE

User: Hello
Output: NONE

User: What are you doing?
Output: NONE

Remember: Return ONLY the fact or EXACTLY the word NONE.
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
    return data["response"]
    

