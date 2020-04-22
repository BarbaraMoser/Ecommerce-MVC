import uuid

from app.utils.string import StringUtils


class Person:

    def __init__(self, name: str, email: str, phone: str, address: str):
        self._id: str = str(uuid.uuid4())
        self._name: str = name
        self._email: str = email
        self._phone: str = phone
        self._address: str = address
        self._active: bool = True

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    def validate(self, **kwargs):
        raise Exception('You need implement this method')

    def _name_is_valid(self, name: str):
        return StringUtils.is_empty_or_is_null(name)

    def _email_is_valid(self, email: str):
        return StringUtils.is_empty_or_is_null(email)

    def _phone_is_valid(self, phone: str):
        return StringUtils.is_empty_or_is_null(phone)

    def _address_is_valid(self, address: str):
        return StringUtils.is_empty_or_is_null(address)
