class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql:///book_store"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    pass
class DevelopmentConfig(Config):
    pass
  
 class TestConfig(Config):
    TESTING = True
