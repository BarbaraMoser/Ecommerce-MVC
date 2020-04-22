from flask import Flask

from app.views.approval_purchase_view import app_approval
from app.views.home_view import home_routes
from app.views.registration_view import app_cadastro
from app.views.login_view import login_routes

app = Flask(__name__)
app.register_blueprint(login_routes)
app.register_blueprint(app_cadastro)
app.register_blueprint(home_routes)
app.register_blueprint(app_approval)

