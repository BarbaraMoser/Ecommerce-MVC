from app.core.repository import Repository


class LegalDao(Repository):
    def __init__(self):
        super().__init__()

    def find_legal_level_by_purchase_amount(self, purchase_amount):
        self._cursor.execute(f"SELECT PROCESS_LEVEL FROM LEGAL_PROCESS_LEVEL WHERE MINIMUM_VALUE <= {purchase_amount} and MAXIMUM_VALUE >= {purchase_amount}")
        process_level = self._cursor.fetchmany(size=1)[0]
        self.close_connection()
        return process_level