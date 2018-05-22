class BaseConfig:
    testing = False


class TestConfig(BaseConfig):
    """
    Test configuration
    """
    pass


class DevelopmentConfig(BaseConfig):
    """
    Dev configuration.
    """
    pass


class ProductionConfig(BaseConfig):
    """
    Production configuration.
    """
    pass
