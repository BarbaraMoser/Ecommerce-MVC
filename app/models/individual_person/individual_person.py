from app.models.person.person import Person
from app.utils.string import StringUtils


class IndividualPerson(Person):

    def __init__(self, name: str, email: str, phone: str, address: str, rg: str, cpf: str, date_of_birth: str):
        # self.validate(name, email, phone, address, rg, cpf, date_of_birth)
        super().__init__(name, email, phone, address)
        self._rg: str = rg
        self._cpf: str = cpf
        self._date_of_birth: str = date_of_birth

    @property
    def rg(self):
        return self._rg

    @rg.setter
    def rg(self, rg):
        self._rg = rg

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    # def validate(self, name: str, email: str, phone: str, address: str, rg: str, cpf: str, date_of_birth: str):
    #     self._name_is_valid(name)
    #     self._email_is_valid(email)
    #     self._rg_is_valid(rg)
    #     self._cpf_is_valid(cpf)
    #     self._date_of_birth_is_valid(date_of_birth)
    #     self._phone_is_valid(phone)
    #     self._address_is_valid(address)
    #
    # def _rg_is_valid(self, rg: str):
    #     return StringUtils.is_empty_or_is_null(rg)
    #
    # def _cpf_is_valid(self, cpf: str):
    #     return StringUtils.is_empty_or_is_null(cpf)
    #
    # def _date_of_birth_is_valid(self, date_of_birth: str):
    #     return StringUtils.is_empty_or_is_null(date_of_birth)
