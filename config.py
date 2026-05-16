import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()


class Config:

    SECRET_KEY = 'secret-key'

    DB_USER = os.getenv('DB_USER')

    DB_PASS = quote_plus(
        os.getenv('DB_PASS')
    )

    DB_HOST = os.getenv('DB_HOST')

    DB_NAME = os.getenv('DB_NAME')

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://"
        f"{DB_USER}:{DB_PASS}"
        f"@{DB_HOST}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False