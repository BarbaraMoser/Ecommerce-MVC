from importlib.resources import Resource

from app.models.facade_approval.facade_approval import FacadeApproval
from app.models.messages.factory_message import FactoryMessages
from app.models.purchase_order.purchase_order import PurchaseOrder
from app.models.purchase_order.purchase_order_dao import PurchaseOrderDao


class PurchaseOrderController:
    _individual_person_dao = PurchaseOrderDao()

    def verify_approval(self, request):
        purchase = PurchaseOrder(
            total_purchase_amount=request['total_purchase_amount'],
            status_purchase=request['status_purchase'],
            client_id=request['client_id']
        )
        purchase_status = FacadeApproval.return_credit_situation(purchase)
        return FactoryMessages.get_message(request['message_type'], purchase_status)

    def create_new_purchase(self, request):
        purchase = PurchaseOrder(
            total_purchase_amount=request['total_purchase_amount'],
            status_purchase=request['status_purchase'],
            client_id=request['client_id']
        )
        self._individual_person_dao.create(purchase)
        return purchase
