import uuid
from typing import Final

from app.utils.string import StringUtils


class Login:
    # _instance = None
    _MINIMUN_NUMBER_OF_CHARACTERS: Final = 8

    def __init__(self, username: str, password: str, person_id: str):
        self._id: str = uuid.uuid4()
        self._username: str = username
        self._password: str = password
        self._person_id: str = person_id

    # @staticmethod
    # def get_instance():
    #     if not Login.__instance:
    #         Login.__instance = Login()
    #     return Login.__instance

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
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, person_id):
        self._person_id = person_id

    def validate(self, username: str, password: str):
        self._username_is_valid(username)
        self._password_is_valid(password)

    def _username_is_valid(self, username: str):
        return StringUtils.is_empty_or_is_null(username)

    def _password_is_valid(self, password: str):
        if not StringUtils.is_empty_or_is_null(password):
            self._password_has_minimum_of_characters(password)

    def _password_has_minimum_of_characters(self, password: str):
        if not len(password) >= self._MINIMUN_NUMBER_OF_CHARACTERS:
            raise Exception('The password must be 8 or more characters')
        return True

    # def validate_login(self, username: str, password: str):
    #     saved_user = self._validate_username(username)
    #     if not password == saved_user.get_password():
    #         raise Exception('Senha incorreta')
    #     return self.create(username, password)
    #
    # def _validate_username(self, username: str) -> Person:
    #     user_controller = UserController()
    #     saved_user = user_controller.find_user(username)
    #     if not len(saved_user):
    #         raise Exception('Usuário não encontrado')
    #     return saved_user[0]
