from flask import Flask

from app import pages

from flask import *

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.register_blueprint(pages.bp)
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['UPLOAD_FOLDER'] = 'static/uploads'
    return app