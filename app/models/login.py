import uuid

from DateTime import DateTime


class Login:
    _instance = None

    def __init__(self):
        self._id = uuid.uuid4()
        self._username = ''
        self._password = ''
        self._logged_in = DateTime.now()

    @staticmethod
    def get_instance():
        if not Login.__instance:
            Login.__instance = Login()
        return Login.__instance

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def logged_in(self):
        return self._logged_in

    @logged_in.setter
    def logged_in(self, logged_in):
        self._logged_in = logged_in

    def validate_login(self, username: str, password: str):
        saved_user = self._validate_username(username)
        if not password == saved_user.get_password():
            raise Exception('Senha incorreta')
        return self.create(username, password)

    # def _validate_username(self, username: str) -> User:
    #     user_controller = UserController()
    #     saved_user = user_controller.find_user(username)
    #     if not len(saved_user):
    #         raise Exception('Usuário não encontrado')
    #     return saved_user[0]
