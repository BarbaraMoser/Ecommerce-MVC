from flask import Blueprint, render_template

from app.models.integrations.xml_files_integration import XmlFilesIntegration

file_routes = Blueprint('app.file', __name__)


@file_routes.route('/file/<id_city>', methods=['GET'])
def find_city_by_id(id_city):
    city = XmlFilesIntegration.find_info_by_id(id_city)
    return render_template('index.html')
