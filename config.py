""" Configuration for the application """


class Config(object):
    """
        Class contains basic configuration settings that other configurations
        will inherit from
    """


class ProductionConfig(Config):
    """
        Configuration for production
    """
    DEBUG = False
    SECRET_KEY = "dfth646fd6f2"


class DevelopConfig(Config):
    """
        Configuration for development
    """
    DEBUG = True
    SECRET_KEY = "dfth642"


class TestingConfig(Config):
    """
        Configuration for testing
    """
    Testing = True
    DEBUG = True
    SECRET_KEY = "dfth642"
    WTF_CSRF_ENABLED = False


app_config = {
    'production': ProductionConfig(),
    'testing': TestingConfig(),
    'development': DevelopConfig()
}
