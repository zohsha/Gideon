from brain import ask_gideon

print("Gideon online. How may I assist you?")

while True:
    user_input = input("You:")

    if user_input.lower() == "exit":
        print("Gideon: Goodbye, Zohaib.")
        break
    
    response = ask_gideon(user_input)
    print(f"Gideon: {response}")