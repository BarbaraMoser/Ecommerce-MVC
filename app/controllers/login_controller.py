from flask_restful import Resource, reqparse

from app.models.login.login import Login
from app.models.login.login_dao import LoginDao


class LoginController(Resource):
    def __init__(self):
        self._login_dao = LoginDao()

    def create_new_login(self, request, person_id):
        new_login = Login(
            username=request.form['username'],
            password=request.form['password'],
            person_id=person_id.id
        )
        self._login_dao.create(new_login)

    def put(self, id):
        args = self.request_parce.parse_args()
        login = Login().get_instance()
        login.id = id
        login.password = args['password']
        return self._login_dao.update(login), 201

    def delete(self, id):
        self._login_dao.delete(id)
        return '', 204
