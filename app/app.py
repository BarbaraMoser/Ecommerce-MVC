from flask import Flask

from app.views.login_view import login_routes

app = Flask(__name__)
app.register_blueprint(login_routes)
