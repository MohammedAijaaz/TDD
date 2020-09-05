import pytest
from backend.src.app import Todos

@pytest.fixture()
def create_todos():
    todos = Todos()
    yield todos

    del todos
