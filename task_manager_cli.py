import argparse
import pprint
import json
import os
from datetime import date

today = str(date.today())

# [
#   {
#       "id": last_index,
#       "desc":
#       "status":
#       "created_at":
#       "update_at":
#   },
#   ...
# ]

data = []

# Functions
def task_add(args):
    last_index = len(data)
    data.append({"id": last_index,
                 "desc": args.desc,
                 "status": args.status,
                 "created_at": today,
                 "updated_at": "Not yet updated"})
    print(f"Task added successfully (ID: {last_index})")

def task_delete(args):
    data.pop(args.id_del)
    print(f"Task deleted (ID: {args.id_del})") 

def task_update(args):
    data[args.id_upd] = {}
    print(f"Task updated (ID: {args.id_upd})")

def task_list(args):
    if args.tag == "todo":
        print_tasks(data, args.tag)
    elif args.tag == "done":
        print_tasks(data, args.tag)
    elif args.tag == "in-progress":
        print_tasks(data, args.tag)
    else:
        print_tasks(data, "all")

def print_tasks(data_task, argument):
    print("ID".ljust(5, "-") + 
      "DESCRIPTION".ljust(50, "-") +
      "STATUS".ljust(14, "-") +
      "CREATED AT".ljust(13, "-") +
      "UPDATED AT".ljust(10, "-"))
    if argument == "all":
        for i in range(len(data)):
            text_format(data, i)
    for i in range(len(data)):
        if data_task[i]["status"] == argument:
            text_format(data, i)

def text_format(data_task, index):
    print(f"{str(data_task[index]["id"]).ljust(5, ".")}" + 
          f"{str(data_task[index]["desc"]).ljust(50, ".")}" +
          f"{str(data_task[index]["status"]).ljust(14, ".")}" +
          f"{str(data_task[index]["created_at"]).ljust(13, ".")}" +
          f"{str(data_task[index]["updated_at"]).ljust(10, ".")}")

# Saving data
def load_file():
    if not os.path.exists("data.json"):
        return []
    with open("data.json", "r") as f:
        return json.load(f)

def save_file(list):
    with open("data.json", "w") as f:
        json.dump(data, f)

# Main function
def main():

    parser = argparse.ArgumentParser(
        prog        = "task-manager",
        description = "A program made to help organizing the tasks")
    
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser("add", help="Add a task")
    parser_add.add_argument("desc", help="Description of the task")
    parser_add.add_argument("status", help="The current status of the task",
                             choices=["todo", "done", "in-progress", "all"])
    parser_add.set_defaults(func=task_add)

    parser_delete = subparsers.add_parser("delete", help="Deletes a task")
    parser_delete.add_argument("id_del", help="ID of the task for delete")
    parser_delete.set_defaults(func=task_delete)

    parser_update = subparsers.add_parser("update", help="Updates the status of a task")
    parser_update.add_argument("id_upd", help="ID of the task for update")
    parser_update.add_argument("desc", help="Description of the task")
    parser_update.set_defaults(func=task_update)

    parser_list = subparsers.add_parser("list", help ="List tasks")
    parser_list.add_argument("tag", help="The status of the task",
                             nargs="?",
                             choices=["todo", "done", "in-progress", "all"], 
                             default="all")
    parser_list.set_defaults(func=task_list)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    data = load_file()
    main()
    save_file(data)