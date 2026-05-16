from app.models.user import User
from app.extensions import db, bcrypt

class AuthService:

    @staticmethod
    def register(name, email, password):

        hashed = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        user = User(
            name=name,
            email=email,
            password=hashed
        )

        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def authenticate(email, password):

        user = User.query.filter_by(
            email=email
        ).first()

        if user and bcrypt.check_password_hash(
            user.password,
            password
        ):
            return user

        return None