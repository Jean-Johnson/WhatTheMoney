from flask import render_template

def method_not_allowed(e):
    return {"success":False,"error":"check the url"}, 405