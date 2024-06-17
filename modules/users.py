from modules.endpoints import Endpoints as _Endpoints
from modules.todos import Todos


class _User:
    def __init__(self, env: str, details: dict):
        self._env = env
        self.id: int = details['id']
        self.name: str = details['name']
        self.address: dict = details['address']

        self._todo_obj = Todos(env=env)

    @property
    def coordinates(self) -> tuple[str, str]:
        latitude = self.address['geo']['lat']
        longitude = self.address['geo']['lng']
        coordinates = (latitude, longitude)
        return coordinates

    @property
    def todo(self) -> dict:
        return self._todo_obj.todo(user_id=self.id)


class Users:
    def __init__(self, env: str):
        self._env = env
        self._endpoints = _Endpoints(self._env)
        self._users: dict[int, _User] | {} = {}

    def _refresh_users(self):
        response = self._endpoints.users
        response_json = response.json()
        if response_json:
            for _dict in response_json:
                self._users[_dict['id']] = _User(self._env, _dict)

    @property
    def users(self) -> dict[int, _User]:
        if not self._users:
            self._refresh_users()
        return self._users

    def get_users_lying_between(self, latitude: tuple[float | int, float | int],
                                longitude: tuple[float | int, float | int]) -> list[_User]:
        list_of_users = []
        for user in self.users.values():
            cordinates = user.coordinates
            if ((latitude[0] < float(cordinates[0]) < latitude[1])
                    and (longitude[0] < float(cordinates[1]) < longitude[1])):
                list_of_users.append(user)
        return list_of_users
