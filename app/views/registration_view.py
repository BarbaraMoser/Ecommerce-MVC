from typing import Type

from flask import Blueprint, render_template, request, redirect

from app.controllers.business_person_controller import BusinessPersonController
from app.controllers.individual_person_controller import IndividualPersonController
from app.controllers.login_controller import LoginController
from app.models.person.person import Person

app_cadastro = Blueprint('app.cadastro', __name__)


@app_cadastro.route('/cadastros')
def cadastro():
    return render_template('cadastro.html')


@app_cadastro.route('/salvar_cadastro', methods=['POST'])
def salvar_cadastro():
    saved_person_id: Type[Person]
    individual_person_controller = IndividualPersonController()
    business_person_controller = BusinessPersonController()
    login_controller = LoginController()
    type_of_person = request.form['tipo_pessoa']
    try:
        if type_of_person == 'ip':
            saved_person_id = individual_person_controller.create_new_individual_person(request.form)
        if type_of_person == 'bp':
            saved_person_id = business_person_controller.create_new_business_person(request.form)
        login_controller.create_new_login(request, saved_person_id)
        return redirect('/access_allowed')
    except:
        return redirect('/access_denied')
