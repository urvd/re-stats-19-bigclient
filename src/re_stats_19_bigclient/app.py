import json
from os import  path;

from flask import Flask

from src.re_stats_19_bigclient.ApiManagement.requests_api import CallsApi
app = Flask(__name__)
players = CallsApi().playersListCalls(season="2017-2018", club_id="529")

@app.route('/')
def authent():
    return "hello the world"

@app.route('/players')
def playersProcess():
    return players

