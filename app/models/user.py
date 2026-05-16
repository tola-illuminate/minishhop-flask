from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from datetime import datetime


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(255),
        nullable=False
    )

    email = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(50),
        default='customer'
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # RELATIONSHIP
    orders = db.relationship(
        'Order',
        back_populates='user'
    )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(
            self.password,
            password
        )