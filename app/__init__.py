from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config
from .init_load import InitLoad

bootstrap = Bootstrap()
init_load =  InitLoad()
from .main import main as main_blueprint
from .main import errors

def create_app(config_name):
    app = Flask(__name__,static_url_path="",static_folder="static")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    init_load.init_objects(app)
    app.register_blueprint(main_blueprint)
    app.register_error_handler(405,errors.method_not_allowed)
    return app