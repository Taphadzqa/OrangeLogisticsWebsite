from flask import Flask
from logging import FileHandler, WARNING  # Error logging
from orange.core.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    if not app.debug:
        error_file_handler = FileHandler(app.root_path + '/core/errorLog.txt')
        error_file_handler.setLevel(WARNING)
        app.logger.addHandler(error_file_handler)

    from orange.routes.errors.handlers import errors
    from orange.routes.main.routes import main
    from orange.routes.hook.routes import webhook
    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(webhook)

    return app
