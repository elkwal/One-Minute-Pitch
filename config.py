import os

class Config:
    '''
    General configuration parent class
    '''
    #
    # SECRET_KEY = None
    # SQLALCHEMY_DATABASE_URI = None
    # UPLOADED_PHOTOS_DEST = None


    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = 'os.environ.get'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:21336622@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'One Minute Pitch'
    SENDER_EMAIL = 'elukwal3@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:21336622@localhost/pitch_test'
