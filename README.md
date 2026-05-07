# TaskManagerCLI
This is a project of a CLI task manager made to be used on the command line.

It has basic commands with their positional arguments (PA) for organizing tasks:
- **`add`**     Add a new task on the list. You need to specify the description (PA - `desc`) and if you want to set the status other than todo, just add the optional `{done, todo, in-progress}` after
- **`delete`**  Delete a task with the specified idd (PA - `id_del`)
- **`update`**  Update a task already created with the id of the task (PA - `id_upd`) and the description (PA - `desc`) you want to change
- **`list`**    List all tasks but you can specify which ones you would like to see (PA - `{todo, done, in-progress}`)
- **`mark`**    Mark a task with a new status (PA - `{done, in-progress}`) followed with the id (PA - `{done, in-progress}`) of the task

### Examples:
```py task-cli.py add "Buy Milk"
#Output: Task added successfully (ID: 0)

py task-cli.py update 0 "Buy Milk and get the kids"
#Output: Task updated (ID: 0)

py task-cli.py delete 0
#Output: Task deleted (ID: 0)

py task-cli.py list
#Listing tasks by status
py task-cli.py list "done"
py task-cli.py list "todo"
py task-cli.py list "in-progress"
```
