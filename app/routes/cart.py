from flask import (
    Blueprint,
    redirect,
    url_for,
    render_template
)

from app.services.cart_service import CartService

cart_bp = Blueprint(
    "cart",
    __name__,
    url_prefix="/cart"
)

@cart_bp.route("/")
def index():

    return render_template(
        "cart/index.html",
        cart=CartService.get_cart(),
        total=CartService.total()
    )

@cart_bp.route("/add/<int:id>")
def add(id):

    CartService.add(id)

    return redirect(
        url_for("cart.index")
    )

@cart_bp.route("/remove/<int:id>")
def remove(id):

    CartService.remove(id)

    return redirect(
        url_for("cart.index")
    )