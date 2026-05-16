from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

from app.services.product_service import ProductService

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

@admin_bp.route("/products")
def products():

    products = ProductService.get_all()

    return render_template(
        "admin/products.html",
        products=products
    )

@admin_bp.route(
    "/products/create",
    methods=["GET", "POST"]
)
def create_product():

    if request.method == "POST":

        ProductService.create(request.form)

        return redirect(
            url_for("admin.products")
        )

    return render_template(
        "admin/create_product.html"
    )

@admin_bp.route("/products/delete/<int:id>")
def delete_product(id):

    product = ProductService.get_by_id(id)

    ProductService.delete(product)

    return redirect(
        url_for("admin.products")
    )