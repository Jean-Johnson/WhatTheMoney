import sys


sys.path.append(".")
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    TEST ="test124"
    MONGO_URI = "mongodb://localhost:27017/myDatabase"

config = {
    "dev":DevConfig
}