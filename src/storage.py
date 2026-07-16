import json

def load_memory():
    with open("data/memory.json", "r") as file:
        data = json.load(file)
        return data
    
def add_fact(fact):
    memory = load_memory()
    # print(memory)
    fact = fact.strip().rstrip(".")
    if fact in memory["facts"]:
        print("memory already there")
    else:
        memory["facts"].append(fact)
        save_memory(memory)

def save_memory(Data):
    with open ("data/memory.json", "w") as file:
        json.dump(Data, file, indent=4)

def get_facts():
    return load_memory()["facts"]
