import argparse
import pprint

# ID : {Title: "", tag: ""}
tasks = {1:{"Title": "Buy groceries", "tag": "todo"},
         2:{"Title": "Buy milk", "tag": "in-progress"},
         3:{"Title": "Shave", "tag": "done"}}

# Functions
def task_add(args):
    print("Task added successfully (ID: 1)")

def task_delete(args):
    print("Task deleted (ID: 1)")

def task_update(args):
    print("Task updated (ID: 1)")

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
    parser_add.set_defaults(func=task_add)

    parser_delete = subparsers.add_parser("delete", help="Deletes a task")
    parser_delete.set_defaults(func=task_delete)

    parser_update = subparsers.add_parser("update", help="Updates the status of a task")
    parser_update.set_defaults(func=task_update)

    parser_list = subparsers.add_parser("list", help ="List tasks")
    parser_list.add_argument("tag", nargs="?",
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