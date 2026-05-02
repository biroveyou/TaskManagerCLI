import argparse

def task_add(args):
    print("Task added successfully (ID: 1)")

def task_delete(args):
    print("Task deleted (ID: 1)")

def task_update(args):
    print("Task updated (ID: 1)")

def main(): 
    parser = argparse.ArgumentParser(
        prog        = "task-manager",
        description = "A program made to help organizing the tasks")
    
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser("add", help="Add a task")
    parser_add.set_defaults(func=task_add)

    parser_delete = subparsers.add_parser("delete", help="deletes a task")
    parser_delete.set_defaults(func=task_delete)

    parser_update = subparsers.add_parser("update", help="Updates the status of a task")
    parser_update.set_defaults(func=task_update)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()