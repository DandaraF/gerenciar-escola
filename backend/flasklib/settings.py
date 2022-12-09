from decouple import config


class Settings:
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
