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

data_task = []

print("ID".ljust(5, "-") + 
      "DESCRIPTION".ljust(50, "-") +
      "STATUS".ljust(14, "-") +
      "CREATED AT".ljust(13, "-") +
      "UPDATED AT".ljust(10, "-"))

print(f"{str(10).ljust(5, ".")}" +
      f"{str("Buy milk").ljust(50, ".")}" +
      f"{str("Done").ljust(14, ".")}" +
      f"{str("2026-05-04").ljust(13, ".")}" +
      f"{str("Not yet").ljust(10, ".")}")

print(f"{str(10).ljust(5, ".")}" +
      f"{str("Go to the supermarket").ljust(50, ".")}" +
      f"{str("In-progress").ljust(14, ".")}" +
      f"{str("2026-05-04").ljust(13, ".")}" +
      f"{str("Not yet").ljust(10, ".")}")