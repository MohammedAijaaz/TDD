class Todo:

    def __init__(self, title):
        self.title = title
        self.complete = False

    def mark_as_complete(self):
        self.complete = True

    def is_complete(self):
        return self.complete


class Todos:

    def __init__(self):
        self.todo_list = []

    def add(self, title="Untitled"):
        self.todo_list.append(Todo(title=title))

    def size(self):
        return len(self.todo_list)

    def get(self, title=None):
        if title:
            found = False
            for todo in self.todo_list:
                if todo.title == title:
                    found = True
                    return todo
            if found == False:
                raise NotFoundException
        else:
            return self.todo_list


    def delete(self, title=None):
        if title:
            iterator = filter(lambda todo: todo.title == title, self.todo_list)
            self.todo_list = list(iterator)
            print(self.todo_list)
        else:
            self.todo_list = []



class NotFoundException(Exception):
    pass