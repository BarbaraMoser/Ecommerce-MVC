from app.core.repository import Repository


class SerasaDao(Repository):
    def __init__(self):
        super().__init__()

    def find_score_by_client_id(self, client_id: str):
        self._cursor.execute(f"SELECT SCORE FROM SERASA_SCORE WHERE CLIENT_ID={client_id}")
        score = self._cursor.fetchmany(size=1)[0]
        self.close_connection()
        return score