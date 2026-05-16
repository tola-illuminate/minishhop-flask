from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()

migrate = Migrate()

login_manager = LoginManager()


def create_app():

    app = Flask(__name__)

    app.config.from_object('config.Config')

    # INIT DATABASE
    db.init_app(app)

    # INIT MIGRATION
    migrate.init_app(app, db)

    # INIT LOGIN
    login_manager.init_app(app)

    # IMPORT MODELS
    from app.models.user import User
    from app.models.product import Product
    from app.models.order import Order
    from app.models.order_item import OrderItem

    return app