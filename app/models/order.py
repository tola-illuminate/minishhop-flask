from app import db
from datetime import datetime


class Order(db.Model):

    __tablename__ = 'orders'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    total_price = db.Column(
        db.Float,
        nullable=False
    )

    phone = db.Column(
        db.String(20),
        nullable=False
    )

    address = db.Column(
        db.Text,
        nullable=False
    )

    payment_image = db.Column(
        db.String(255)
    )

    status = db.Column(
        db.String(50),
        default='Pending'
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # RELATIONSHIP
    user = db.relationship(
        'User',
        back_populates='orders'
    )

    order_items = db.relationship(
        'OrderItem',
        back_populates='order'
    )