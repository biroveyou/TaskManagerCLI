import argparse
import pprint
import json
from datetime import date

today = date.today()

# ID : {Title: "", tag: ""}
tasks = {}
json.dumps(tasks)
index = 1

# Functions
def task_add(args):
    if tasks == {}:
        last_index = 1
    else:
        last_index = (list(tasks.keys())[-1]) + 1
    tasks[last_index] = {"desc": args.desc, 
                         "status": args.status, 
                         "created_at": today, 
                         "updated_at": ""}
    print(f"Task added successfully (ID: {last_index})")

def task_delete(args):
    tasks.pop(args.id_del)
    print(f"Task deleted (ID: {args.id_del})")

def task_update(args):
    tasks[args.id_upd] = {}
    print(f"Task updated (ID: {args.id_upd})")

def task_list(args):
    if args.tag == "todo":
        for k, v in tasks.items():
            if tasks[k]["tag"] == args.tag:
                print(tasks[k])
    elif args.tag == "done":
        for k, v in tasks.items():
            if tasks[k]["tag"] == args.tag:
                print(tasks[k])
    elif args.tag == "in-progress":
        for k, v in tasks.items():
            if tasks[k]["tag"] == args.tag:
                print(tasks[k])
    else:
        pprint.pprint(tasks)

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
    main()