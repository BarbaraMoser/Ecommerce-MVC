from app.models.legal.legal_dao import LegalDao


class Legal:
    _legal_dao = LegalDao()

    @classmethod
    def return_process_level(cls, purchase_amount):
        return cls._legal_dao.find_legal_level_by_purchase_amount(purchase_amount)