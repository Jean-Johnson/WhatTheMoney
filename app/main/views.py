import os
import time
from urllib import request
from flask import config,json, request, Response
from flask import current_app as app
import pandas as pd
import requests
from app import init_load
from . import main
from .. import init_load

@main.route("/health")
def health():
    app.logger.info("health loading")
    app.logger.info(app.config["TEST"])
    return Response(json.dumps({"status":"UP and runnig"}),status=200,mimetype="application/json")
