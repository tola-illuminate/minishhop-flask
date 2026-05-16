from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user
)

from app.services.auth_service import AuthService

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        AuthService.register(
            request.form["name"],
            request.form["email"],
            request.form["password"]
        )

        flash("Register success")

        return redirect(
            url_for("auth.login")
        )

    return render_template("auth/register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        user = AuthService.authenticate(
            request.form["email"],
            request.form["password"]
        )

        if user:

            login_user(user)

            return redirect(
                url_for("public.home")
            )

        flash("Invalid credentials")

    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():

    logout_user()

    return redirect(
        url_for("public.home")
    )