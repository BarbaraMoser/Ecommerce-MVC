from app.models.serasa.serasa_dao import SerasaDao


class Serasa:
    _serasa_dao = SerasaDao()

    @classmethod
    def return_serasa_situation(cls, client_id: str):
        return cls._serasa_dao.find_score_by_client_id(client_id)
