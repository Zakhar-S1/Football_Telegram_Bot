import requests
import json
import config
import pprint
import http.client

s = requests.Session()

headers = {"X-Auth-Token": config.football_key}

def get_connection():

    return http.client.HTTPConnection("api.football-data.org")

def get_standings_CL(connection):

    connection.request("GET", "/v2/competitions/{}/standings".format('CL'), None, headers)
    return json.loads(connection.getresponse().read().decode())

def get_standings_PL(connection):

    connection.request("GET", "/v2/competitions/{}/standings".format('PL'), None, headers)
    return json.loads(connection.getresponse().read().decode())

def get_standings_PD(connection):

    connection.request("GET", "/v2/competitions/{}/standings".format('PD'), None, headers)
    return json.loads(connection.getresponse().read().decode())

def get_matches(connection):

    connection.request("GET", "/v2/matches".format(), None, headers)
    return json.loads(connection.getresponse().read().decode())

def get_player(connection,value):

    connection.request("GET", "/v2/players/{}".format(value), None, headers)
    return json.loads(connection.getresponse().read().decode())
