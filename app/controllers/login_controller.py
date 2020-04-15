from flask_restful import Resource, reqparse

from app.dao.login_dao import LoginDao
from app.models.login import Login


class LoginController(Resource):
    def __init__(self):
        self.request_parce = reqparse.RequestParser()
        self.request_parce.add_argument('username')
        self.request_parce.add_argument('password')
        self._login_dao = LoginDao()

    def post(self):
        args = self.request_parce.parse_args()
        login = Login().get_instance()
        login.username = args['username']
        login.password = args['password']
        return self._login_dao.create(login), 201

    def put(self, id):
        args = self.request_parce.parse_args()
        login = Login().get_instance()
        login.id = id
        login.password = args['password']
        return self._login_dao.update(login), 201

    def delete(self, id):
        self._login_dao.delete(id)
        return '', 204
