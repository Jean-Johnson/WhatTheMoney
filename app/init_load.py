import os
from os import path
from flask import Flask
from flask_pymongo import PyMongo

class InitLoad:
    def __init__(self,app=None) -> None:
        if isinstance(app,Flask):
            self.config =app.config
        else:
            self.config =None

    def init_objects(self,app=None):
        if isinstance(app,Flask):
            app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
            self.config =app.config
        else:
            raise TypeError("APP not initialized")
        self.mongo = PyMongo(app)
        self.test = self.config["TEST"]
        app.logger.info("[+]All loaded.....")