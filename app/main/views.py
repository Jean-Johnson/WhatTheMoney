import os
import time
from urllib import request
from flask import config,json, request, Response
from flask import current_app as app
# import pandas as pd
# import requests
from app import init_load
from . import main
from .. import init_load
from manager import m_manage

@main.route("/health")
def health():
    app.logger.info("health loading")
    app.logger.info(app.config['TEST'])
    return Response(json.dumps({"status":"UP and runnig"}),status=200,mimetype="application/json")

@main.route('/mongo_data/', methods=['GET'])
def get_data():
    data = m_manage.read_mongo()
    for record in data:
        print(record)
    return "Got"
