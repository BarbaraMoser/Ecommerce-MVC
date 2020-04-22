from app.core.repository import Repository
from app.models.business_person.business_person import BusinessPerson


class BusinessPersonDao(Repository):
    def __init__(self):
        super().__init__()

    def create(self, person: BusinessPerson):
        self._cursor.execute(
            f"INSERT INTO BUSINESS_PERSON (ID, NAME, EMAIL, PHONE, ADDRESS, CNPJ, STATE_REGISTRATION) VALUES ("
            f"'{person.id}',"
            f"'{person.name}',"
            f"'{person.email}',"
            f"'{person.phone}',"
            f"'{person.address}',"
            f"'{person.cnpj}',"
            f"'{person.state_registration}')"
        )
        self._conexao.commit()
        self._conexao.close()
