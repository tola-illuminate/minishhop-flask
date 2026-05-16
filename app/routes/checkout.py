from flask import (
    Blueprint,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from app.services.cart_service import CartService
from app.services.order_service import OrderService

checkout_bp = Blueprint(
    "checkout",
    __name__,
    url_prefix="/checkout"
)

@checkout_bp.route("/")
@login_required
def checkout():

    cart = CartService.get_cart()

    total = CartService.total()

    OrderService.create_order(
        current_user.id,
        cart,
        total
    )

    CartService.clear()

    flash("Order placed successfully")

    return redirect(
        url_for("public.home")
    )