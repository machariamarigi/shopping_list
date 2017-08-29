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


class DevelopConfig(Config):
    """
        Configuration for development
    """
    DEBUG = True


class TestingConfig(Config):
    """
        Configuration for testing
    """


app_config = {
    'production': ProductionConfig(),
    'testing': TestingConfig(),
    'development': DevelopConfig()
}