from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import ProductionConfig

api = Api()
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config=ProductionConfig):
    from .resources.routes import initialize_routes

    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    initialize_routes(api)
    api.init_app(app)




