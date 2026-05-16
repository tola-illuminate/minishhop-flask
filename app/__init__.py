from flask import Flask

from app.extensions import (
    db,
    migrate,
    login_manager
)

from app.config import Config


def create_app():

    app = Flask(__name__)

    # LOAD CONFIG
    app.config.from_object(Config)

    # INIT EXTENSIONS
    db.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)

    # LOGIN CONFIG
    login_manager.login_view = "auth.login"

    login_manager.login_message_category = "warning"

    # UPLOAD FOLDER
    app.config["UPLOAD_FOLDER"] = "app/static/uploads"

    # IMPORT MODELS
    from app.models.user import User
    from app.models.product import Product
    from app.models.order import Order
    from app.models.order_item import OrderItem

    # USER LOADER
    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(int(user_id))

    # REGISTER BLUEPRINTS
    from app.routes.public import public_bp
    from app.routes.auth import auth_bp
    from app.routes.cart import cart_bp
    from app.routes.checkout import checkout_bp
    from app.routes.customer import customer_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(public_bp)

    app.register_blueprint(auth_bp)

    app.register_blueprint(cart_bp)

    app.register_blueprint(checkout_bp)

    app.register_blueprint(customer_bp)

    app.register_blueprint(admin_bp)

    return app