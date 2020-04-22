from validate_docbr import CNPJ

from app.models.business_person.business_person import BusinessPerson
from app.models.business_person.business_person_dao import BusinessPersonDao
from app.utils.string import StringUtils


class BusinessPersonController:
    _business_person_dao = BusinessPersonDao()
    _validate_cnpj = CNPJ()

    def cnpj_is_valid(self, value: str):
        if not StringUtils.is_empty_or_is_null(value):
            self._validate_cnpj.validate(value)

    def create_new_business_person(self, request):
        new_person = BusinessPerson(
            name=request['name'],
            email=request['email'],
            phone=request['number'],
            address=request['location'],
            cnpj=request['cnpj'],
            state_registration=request['state_registration'],
        )
        self._business_person_dao.create(new_person)
        return new_person