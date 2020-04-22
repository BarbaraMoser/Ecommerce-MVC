from app.models.credit.credit import Credit
from app.models.legal.legal import Legal
from app.models.purchase_order.purchase_order import PurchaseOrder
from app.models.serasa.serasa import Serasa


class FacadeApproval:
    _SERASA_LOW_RISK = 1000
    _SERASA_MEDIUM_RISK = 700
    _SERASA_HIGH_RISK = 300

    @classmethod
    def return_credit_situation(cls, puchase: PurchaseOrder):
        process_level = Legal.return_process_level(puchase.total_purchase_amount)
        serasa_situation = Serasa.return_serasa_situation(puchase.client_id)
        credit_limit = Credit.return_available_credit_limit(puchase.client_id)
        limit_used = Credit.return_credit_limit_used(puchase.client_id)

        if not cls._credit_limit_available(credit_limit,
                                           limit_used) > puchase.total_purchase_amount or serasa_situation <= cls._SERASA_HIGH_RISK or process_level == 3:
            return False
        return True

    def _credit_limit_available(self, credit_limit, limit_used):
        return credit_limit - limit_used
