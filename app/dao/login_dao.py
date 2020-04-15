from app.core.repository import Repository
from app.models.login import Login


class LoginDao(Repository):
    def __init__(self):
        super().__init__()

    def find_by_username(self, username: str):
        self._cursor.execute(f"SELECT * FROM LOGIN WHERE USERNAME={username}")
        login_saved = self._cursor.fetchmany(size=1)[0]
        login = Login().get_instance()
        login.id = login_saved[0]
        login.username = login_saved[1]
        login.password = login_saved[2]
        self.close_connection()
        return login.__dict__

    def create(self, login: Login):
        self._cursor.execute(
            f"INSERT INTO LOGIN (ID, USERNAME, PASSWORD, LOGGED_IN) VALUES ("
            f"'{login.id}',"
            f"'{login.username}',"
            f"'{login.password}',"
            f"'{login.logged_in}')"
        )
        self.save()
        return login.__dict__

    def update(self, login: Login):
        self._cursor.execute(
            f"UPDATE LOGIN SET PASSWORD = '{login.password}' WHERE ID = {login.id}")
        self.save()
        return login.__dict__

    def delete(self, id: int):
        self._cursor.execute(f"DELETE FROM LOGIN WHERE ID = {id}")
        self.save()
