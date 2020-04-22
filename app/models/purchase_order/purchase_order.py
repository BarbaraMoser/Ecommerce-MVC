import uuid


class PurchaseOrder:

    def __init__(self, total_purchase_amount, status_purchase, client_id):
        self._id = str(uuid.uuid4())
        self._total_purchase_amount = total_purchase_amount
        self._status_purchase = status_purchase
        self._client_id = client_id

    @property
    def id(self):
        return self._id

    @property
    def total_purchase_amount(self):
        return self._total_purchase_amount

    @total_purchase_amount.setter
    def total_purchase_amount(self, total_purchase_amount):
        self._total_purchase_amount = total_purchase_amount

    @property
    def status_purchase(self):
        return self._status_purchase

    @status_purchase.setter
    def status_purchase(self, status_purchase):
        self._status_purchase = status_purchase

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        self._client_id = client_id
