from flask import Blueprint, render_template, request
from werkzeug.utils import redirect

from app.controllers.login_controller import LoginController

login_routes = Blueprint('app.login', __name__)


@login_routes.route('/')
def login():
    return render_template('login.html')


@login_routes.route('/logins', methods=['POST'])
def save_login():
    try:
        login_controller = LoginController()
        username = request.form['username']
        password = request.form['password']
        login_controller.validate_login(username, password)
        return redirect('/access_allowed')
    except:
        return redirect('/access_denied')


@login_routes.route('/access_allowed')
def access_allowed():
    return render_template('acesso_permitido.html')


@login_routes.route('/access_denied')
def access_denied():
    return render_template('acesso_negado.html')
