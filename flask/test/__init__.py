from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

db = SQLAlchemy()


def create_app():
# def create_app(config_class=Config):
    app = Flask(__name__)
    # app.config.from_object(config_class)
    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    db.init_app(app)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # @app.route('/<name>/<location>')
    # def index(name, location):
    #     user = User(name=name, location=location)
    #     db.session.add(user)
    #     db.session.commit()
    #
    #     return  '<h1>Added New User!</h1>'

    return app