from brain import ask_gideon
from memory import add_message, get_conversation
print("Gideon online. How may I assist you?")

while True:
    user_input = input("You:")

    if user_input.lower() == "exit":
        print("Gideon: Goodbye, Zohaib.")
        break

    add_message("user", user_input)

    response = ask_gideon(get_conversation())
    add_message("assistant", response)
    print(f"Gideon: {response}")
    print(get_conversation())