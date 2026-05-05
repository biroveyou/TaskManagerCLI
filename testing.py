import json
import os

data = []

# Saving data
def load_file():
    if not os.path.exists("data.json"):
        return []
    with open("data.json", "r") as f:
        return json.load(f)

def save_file(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

# Function
def task_add():
    last_index = len(data)
    data.append({"id": last_index,})

data = load_file()
task_add()
save_file(data)

print(data)