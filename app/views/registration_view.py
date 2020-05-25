from typing import Type

from flask import Blueprint, render_template, request, redirect

from app.controllers.api_integration_controller import CepApiIntegrationController
from app.controllers.business_person_controller import BusinessPersonController
from app.controllers.files_integration_controller import FilesIntegrationController
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


@app_cadastro.route('/buscar_cep', methods=['POST'])
def buscar_cep():
    cep = request.form['cep']
    address = CepApiIntegrationController.find_address_by_cep(cep)
    cep = address['cep']
    rua = (u'%s' % address['logradouro'])
    bairro = (u'%s' % address['bairro'])
    cidade = (u'%s' % address['localidade'])
    uf = address['uf']
    ibge = address['ibge']
    return render_template('busca_cep.html', cep=cep, rua=rua, bairro=bairro, cidade=cidade, uf=uf, ibge=ibge)


@app_cadastro.route('/find_city/<id>', methods=['GET'])
def buscar_cidade():
    file_integration_controller = FilesIntegrationController()
    try:
        city = file_integration_controller.txt_integration(str(id))
        return city
    except:
        return 'City not found.'
