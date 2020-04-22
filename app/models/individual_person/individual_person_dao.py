from app.core.repository import Repository
from app.models.individual_person.individual_person import IndividualPerson


class IndividualPersonDao(Repository):
    def __init__(self):
        super().__init__()

    def create(self, person: IndividualPerson):
        self._cursor.execute(
            f"INSERT INTO INDIVIDUAL_PERSON (ID, NAME, EMAIL, PHONE, ADDRESS, RG, CPF, DATE_OF_BIRTH) VALUES ("
            f"'{person.id}',"
            f"'{person.name}',"
            f"'{person.email}',"
            f"'{person.phone}',"
            f"'{person.address}',"
            f"'{person.rg}',"
            f"'{person.cpf}',"
            f"'{person.date_of_birth}')"
        )
        # self.save()
        self._conexao.commit()
        self._conexao.close()

