from app.core.repository import Repository
from app.models.purchase_order.purchase_order import PurchaseOrder


class PurchaseOrderDao(Repository):
    def __init__(self):
        super().__init__()

    def create(self, person: PurchaseOrder):
        self._cursor.execute(
            f"INSERT INTO PURCHASE (ID, TOTAL_PURCHASE_AMOUNT, STATUS_PURCHASE, CLIENT_ID) VALUES ("
            f"'{person.id}',"
            f"'{person.total_purchase_amount}',"
            f"'{person.status_purchase}',"
            f"'{person.client_id}',"
        )
        self._conexao.commit()
        self._conexao.close()
