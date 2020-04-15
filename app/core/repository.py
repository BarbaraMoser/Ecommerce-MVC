import MySQLdb


class Repository:

    def __init__(self):
        self._conexao = MySQLdb.connect(host='localhost', user='root', passwd='root', database='ecommerce')
        self._cursor = self._conexao.cursor()

    def save(self):
        self._conexao.commit()
        self.close_connection()

    def close_connection(self):
        self._conexao.close()
