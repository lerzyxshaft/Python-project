from datetime import datetime

class Todo:
    def __init__(self, name):
        self.id = datetime.now()
        self.name = name
        self.isComplete = False

    # build-in function for displaying data
    def __str__(self):
        return f"[{self.isComplete}] {self.name}]"


class TodoApp:
    def __init__(self):
        self.todos = []

    def add_todo(self):
        # get todo_name from input
        todo_name = input("Enter name of todo: ")
        # create todo
        new_todo = Todo(todo_name)
        # add todo to array
        self.todos.append(new_todo)
        # print successful response
        print(f"Todo was successfully created with name '{new_todo.id}, {new_todo.name}, {new_todo.isComplete}'")

    def display_todos(self):
        # check if user have todos
        if not self.todos:
            print("You don't have any todos")
        for todo in self.todos:
            print("Your todos: ")
            print(todo)

    def mark_as_completed(self):
        print(self.display_todos())
        mark_as_done = input("Chose todo which you wanna mark as done(1, 2, 3,...)")
        mark_as_done = int(mark_as_done)
        mark_as_done = +1
        for mark_as_done in self.todos :
            self.todos.remove(mark_as_done)
        self.run()

    def run(self):
        while True:
            print("Welcome to our app")
            print("Press 1 to create a new to do")
            print("Press 2 to check list of your todo's")
            print("Press 3 to exit the app")
            print("Press 4 to mark as done")
            user_choice = input("Enter your choice: ")
            if user_choice == "1":
                self.add_todo()
            elif user_choice == "2":
                self.display_todos()
            elif user_choice == "3":
                print("Thank you for using our app")
                break
            elif user_choice == "4":
                self.mark_as_completed()
            else:
                print("Invalid choice")


if __name__ == "__main__":
    app = TodoApp()
    app.run()

