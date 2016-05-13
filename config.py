import os


class BaseConfig(object):
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TABLEAU_URL = 'http://10.10.10.10'

class ProductionConfig(BaseConfig):
    DEBUG = False
 
