from importlib.resources import Resource

from app.models.facade_approval.facade_approval import FacadeApproval
from app.models.purchase_order.purchase_order import PurchaseOrder
from app.models.purchase_order.purchase_order_dao import PurchaseOrderDao


class PurchaseOrderController(Resource):
    _individual_person_dao = PurchaseOrderDao()

    def verify_approval(self, request):
        purchase = PurchaseOrder(
            total_purchase_amount=request['total_purchase_amount'],
            status_purchase=request['status_purchase'],
            client_id=request['client_id']
        )
        if not FacadeApproval.return_credit_situation(purchase):
            raise Exception('Purchase is not available')
        return True

    def create_new_purchase(self, request):
        purchase = PurchaseOrder(
            total_purchase_amount=request['total_purchase_amount'],
            status_purchase=request['status_purchase'],
            client_id=request['client_id']
        )
        self._individual_person_dao.create(purchase)
        return purchase
