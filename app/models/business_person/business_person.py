from app.models.person.person import Person
from app.utils.string import StringUtils


class BusinessPerson(Person):

    def __init__(self, name: str, email: str, phone: str, address: str, cnpj: str, state_registration: str):
        super().__init__(name, email, phone, address)
        self._cnpj: str = cnpj
        self._state_registration: str = state_registration

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self._cnpj = cnpj

    @property
    def state_registration(self):
        return self._state_registration

    @state_registration.setter
    def state_registration(self, state_registration):
        self._state_registration = state_registration

    # def validate(self, name: str, email: str, phone: str, address: str, cnpj: str, state_registration: str):
    #     self._name_is_valid(name)
    #     self._email_is_valid(email)
    #     self._cnpj_is_valid(cnpj)
    #     self._state_registration_is_valid(state_registration)
    #     self._phone_is_valid(phone)
    #     self._address_is_valid(address)
    #
    # def _cnpj_is_valid(self, cnpj: str):
    #     return StringUtils.is_empty_or_is_null(cnpj)
    #
    # def _state_registration_is_valid(self, state_registration: str):
    #     return StringUtils.is_empty_or_is_null(state_registration)
