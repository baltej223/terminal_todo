# Terminal ToDo 
A straightforward to-do application that runs on your terminal!
## Installation 
``` git clone https://github.com/baltej223/terminal_todo.git ```

- It will clone this repository to a folder named terminal_todo.
- Then, modify the environment variables on your computer.
## Modifying environment variables
To edit environment variables:
***Currently its only available for Windows***
**Windows**:
1. Open the **Start Menu**, search for **"Environment Variables"**.
2. Click **Edit the system environment variables**.
3. In the System Properties window, click **Environment Variables**.
4. Add path of terminal_todo folder to the path.

**Linux**:
1. Open a terminal.
2. Edit shell configuration files (e.g., `~/.bashrc` or `~/.zshrc`) with a text editor.
3. Add or modify variables, e.g., `export VAR_NAME=value`.
4. Run `source ~/.bashrc` to apply changes.

**Mac**:
1. Open the terminal.
2. Edit files like `~/.bash_profile` or `~/.zshrc`.
3. Add or modify `export VAR_NAME=value`.
4. Reload with `source ~/.zshrc`.

## Working
- basically when you run command ```todo```, it executed a batch file, todo.bat, which runs the python script. 
### Commands
1. ```todo add <todo>``` : It adds the given todo to the todo list
2. ```todo ls``` or ```todo list``` : Both command list the added todos, and works the same way.
3. ```todo edit <todoNumber> <EditedTodo>``` : It edits an already existing todo. 
4. ```todo remove <todoNumber>``` : It remove an already added todo. 

## Examples
```
todo add "task 1"
```
It adds 'task 1' as todo
---
```
todo ls 
```
It will list all the todos.
---
```
todo edit 1 "Task"
```
- It will overwright todo with todo number 1 with "Tasks"
---
```
todo edit 1 ":: n"
```
- If todo 1 was "Task", then running this command will append n after the already existing todo.
---
```
todo remove 1
```
- It will remove todo with todo number 1
---