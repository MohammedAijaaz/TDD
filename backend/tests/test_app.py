
import pytest
from backend.src.app import Todos, NotFoundException


def test_create_empty_todos(create_todos):
    todos = create_todos
    assert todos.size() == 0

def test_add_new_todo(create_todos):
    todos = create_todos
    todos.add(title="Test todo")

    assert todos.size() == 1


def test_add_two_todos(create_todos):
    todos = create_todos
    todos.add(title="first todo")
    todos.add(title="second todo")

    assert todos.size() == 2


def test_add_1_get_1_todo(create_todos):
    todos = create_todos
    
    todos.add(title="first todo")
    all_todos = todos.get()

    assert len(all_todos) == 1

def test_add_multiple_todos_get_x_todo(create_todos):
    todos = create_todos

    todos.add(title="first todo")
    todos.add(title="second todo")
    todos.add(title="third todo")

    todo = todos.get(title="second todo")

    assert todo.title == "second todo"


def test_mark_todo_as_complete(create_todos):
    todos = create_todos

    todos.add(title="first todo")
    todo = todos.get(title="first todo")
    assert todo.is_complete() == False
    todo.mark_as_complete()
    assert todo.is_complete() == True


def test_delete_todo(create_todos):
    todos = create_todos

    todos.add(title="first todo")
    todo = todos.get(title="first todo")
    with pytest.raises(NotFoundException):
        todos.delete(todo)
        todos.get(title="first todo")

def test_delete_all_todos(create_todos):
    todos = create_todos

    todos.add(title="first todo")
    todos.add(title="second todo")

    todos.delete()

    assert todos.size() == 0