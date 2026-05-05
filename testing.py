import json
import os

data =  [
            {"id": 0, 
            "desc": "Buy Groceries tomorrow", 
            "status": "todo", 
            "created_at": "2026-05-05", 
            "updated_at": "Not yet updated"}, 

            {"id": 1, 
             "desc": "Buy Groceries tomorrow", 
             "status": "todo", 
             "created_at": "2026-05-05", 
             "updated_at": "Not yet updated"}
        ]
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

def task_delete(tag):
    for v in range(len(data)):
        if data[v]["id"] == tag:
            del data[v]
    print(f"Task deleted (ID: {tag})") 

print(data)
print()
task_delete(1)
print()
print(data)