from modules.endpoints import Endpoints as _endpoints


class _Todo:

    def __init__(self, details: dict):
        self.id: int = details['id']
        self.userId: int = details['userId']
        self.title: str = details['title']
        self.completed: bool = details['completed']


class Todos:
    def __init__(self, env):
        self._endpoints = _endpoints(env)
        self._todo: dict[int, _Todo] = {}

    def _get_all_todos(self) -> list[dict]:
        response = self._endpoints.todos
        return response.json()

    def todo(self, user_id: int) -> dict[int, _Todo]:
        if not self._todo:
            for todo_dict in self._get_all_todos():
                if todo_dict.get('userId') == user_id:
                    self._todo[todo_dict['id']] = _Todo(todo_dict)
        return self._todo
