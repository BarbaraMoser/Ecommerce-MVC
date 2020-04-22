from validate_docbr import CPF

from app.models.individual_person.individual_person import IndividualPerson
from app.models.individual_person.individual_person_dao import IndividualPersonDao
from app.utils.string import StringUtils


class IndividualPersonController:
    _individual_person_dao = IndividualPersonDao()
    _validate_cpf = CPF()

    def cpf_is_valid(self, value: str):
        if not StringUtils.is_empty_or_is_null(value):
            self._validate_cpf.validate(value)

    def create_new_individual_person(self, request):
        new_person = IndividualPerson(
            name=request['name'],
            email=request['email'],
            phone=request['number'],
            address=request['location'],
            rg=request['rg'],
            cpf=request['cpf'],
            date_of_birth=request['date_of_birth'],
        )
        self._individual_person_dao.create(new_person)
        return new_person
