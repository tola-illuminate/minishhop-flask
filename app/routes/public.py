from flask import Blueprint, render_template

from app.services.product_service import ProductService

public_bp = Blueprint(
    "public",
    __name__
)

@public_bp.route("/")
def home():

    products = ProductService.get_all()

    return render_template(
        "public/home.html",
        products=products
    )

@public_bp.route("/product/<int:id>")
def product_detail(id):

    product = ProductService.get_by_id(id)

    return render_template(
        "public/detail.html",
        product=product
    )