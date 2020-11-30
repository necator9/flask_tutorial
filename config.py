import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'custom_and_secure_string'
