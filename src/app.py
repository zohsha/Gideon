from brain import ask_gideon, extract_memory
from memory import add_message, get_conversation
from storage import load_memory, add_fact

print(load_memory())
print("Gideon online. How may I assist you?")

while True:
    user_input = input("You:")

    if user_input.lower() == "exit":
        print("Gideon: Goodbye, Zohaib.")
        break

    add_message("user", user_input)
    memory = extract_memory(user_input)
    print(memory)
    if memory["remember"]:
        for fact in memory["facts"]:
            add_fact(fact)

    response = ask_gideon(get_conversation())
    add_message("assistant", response)
    print(f"Gideon: {response}")
    