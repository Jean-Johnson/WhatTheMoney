import os
from os import path
from flask import Flask

class InitLoad:
    def __init__(self,app=None) -> None:
        if isinstance(app,Flask):
            self.config =app.config
        else:
            self.config =None

    def init_objects(self,app=None):
        if isinstance(app,Flask):
            self.config =app.config
        else:
            raise TypeError("APP not initialized")
        self.test = self.config["TEST"]
        app.logger.info("[+]All loaded.....")