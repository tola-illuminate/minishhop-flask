from flask import (
    Blueprint,
    render_template
)

from flask_login import (
    login_required,
    current_user
)

customer_bp = Blueprint(
    "customer",
    __name__,
    url_prefix="/customer"
)

@customer_bp.route("/orders")
@login_required
def orders():

    return render_template(
        "customer/orders.html",
        orders=current_user.orders
    )