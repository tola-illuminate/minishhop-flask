from app import db
from datetime import datetime


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(255),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    image = db.Column(
        db.String(255)
    )

    stock = db.Column(
        db.Integer,
        default=0
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # RELATIONSHIP
    order_items = db.relationship(
        'OrderItem',
        back_populates='product'
    )