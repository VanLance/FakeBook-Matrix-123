import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABSE_URI = os.environ.get('DATABASE_URL')