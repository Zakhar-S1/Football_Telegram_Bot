from mongodb import db_add_user, db_return_user, db_update_state, db_update_history, db_return_history
from API import get_connection, get_standings_CL, get_standings_PL, get_standings_PD, get_matches, get_player
import pprint
import time

DICT_GROUPS = {'A':'GROUP_A','B':'GROUP_B','C':'GROUP_C','D':'GROUP_D','E':'GROUP_E','F':'GROUP_F','G':'GROUP_G','H':'GROUP_H',}

def registration(message):
    info = {'chat_id':message.chat.id, 'state':'menu', 'history':[]}
    db_add_user(info)

def return_user(message):
    return db_return_user(message)

def update_state(message,menu):
    db_update_state(message,menu)

def table_CL(message):
    answer = []
    mes = ""
    connection = get_connection()
    data = get_standings_CL(connection)

    answer.append("{0} - {1}\nStart: {2} End: {3}\nWinner - {4}".format(data['competition']['area']['name'],data['competition']['name'],data['season']['startDate'],data['season']['endDate'],data['season']['winner']))
    for i in range(0,len(data['standings']),3):
        for j in range(len(data['standings'][i]['table'])):
            if data['standings'][i]['group'] == DICT_GROUPS.get(message.text):
                mes += "Group: {0}\n".format(data['standings'][i]['group'][-1])
                mes += "Name: {0}\nWon: {1}\nDraw: {2}\nLost: {3}\nGoal difference: {4}\nPoints: {5}\nPosition: {6}\nPlayed game: {7}\n".format(data['standings'][i]['table'][j]['team']['name'],
                                                                            data['standings'][i]['table'][j]['won'],
                                                                            data['standings'][i]['table'][j]['draw'],
                                                                            data['standings'][i]['table'][j]['lost'],
                                                                            data['standings'][i]['table'][j]['goalDifference'],
                                                                            data['standings'][i]['table'][j]['points'],
                                                                            data['standings'][i]['table'][j]['position'],
                                                                            data['standings'][i]['table'][j]['playedGames'])
                answer.append(mes)
                mes = ''
    return answer

def table_PL():
    answer = []
    mes = ""
    connection = get_connection()
    data = get_standings_PL(connection)

    answer.append("{0} - {1}\nStart: {2} End: {3}\nWinner - {4}".format(data['competition']['area']['name'],data['competition']['name'],data['season']['startDate'],data['season']['endDate'],data['season']['winner']))
    for j in range(len(data['standings'][0]['table'])):
        mes += "Stage: {0}\n".format(data['standings'][0]['stage'])
        mes += "Name: {0}\nWon: {1}\nDraw: {2}\nLost: {3}\nGoal difference: {4}\nPoints: {5}\nPosition: {6}\nPlayed game: {7}\n".format(data['standings'][0]['table'][j]['team']['name'],
                                                                            data['standings'][0]['table'][j]['won'],
                                                                            data['standings'][0]['table'][j]['draw'],
                                                                            data['standings'][0]['table'][j]['lost'],
                                                                            data['standings'][0]['table'][j]['goalDifference'],
                                                                            data['standings'][0]['table'][j]['points'],
                                                                            data['standings'][0]['table'][j]['position'],
                                                                            data['standings'][0]['table'][j]['playedGames'])
        answer.append(mes)
        mes = ''
    return answer

def table_PD():
    answer = []
    mes = ""
    connection = get_connection()
    data = get_standings_PD(connection)

    answer.append("{0} - {1}\nStart: {2} End: {3}\nWinner - {4}".format(data['competition']['area']['name'],data['competition']['name'],data['season']['startDate'],data['season']['endDate'],data['season']['winner']))
    for j in range(len(data['standings'][0]['table'])):
        mes += "Stage: {0}\n".format(data['standings'][0]['stage'])
        mes += "Name: {0}\nWon: {1}\nDraw: {2}\nLost: {3}\nGoal difference: {4}\nPoints: {5}\nPosition: {6}\nPlayed game: {7}\n".format(data['standings'][0]['table'][j]['team']['name'],
                                                                            data['standings'][0]['table'][j]['won'],
                                                                            data['standings'][0]['table'][j]['draw'],
                                                                            data['standings'][0]['table'][j]['lost'],
                                                                            data['standings'][0]['table'][j]['goalDifference'],
                                                                            data['standings'][0]['table'][j]['points'],
                                                                            data['standings'][0]['table'][j]['position'],
                                                                            data['standings'][0]['table'][j]['playedGames'])
        answer.append(mes)
        mes = ''
    return answer

def matches_today():
    answer = []
    mes = ""
    connection = get_connection()
    data = get_matches(connection)

    answer.append("Day: {0}\n".format(data['filters']['dateFrom']))
    for i in range(len(data['matches'])):
        mes += "Competiton name: {0} \nAway team: {1} - Home team: {2}".format(data['matches'][i]['competition']['name'],
                                                                                data['matches'][i]['awayTeam']['name'],
                                                                                data['matches'][i]['homeTeam']['name'])
        answer.append(mes)
        mes = ''
    return answer

def add_history(message,action):
    db_update_history(message,action)

def return_history(message):
    answer = ''
    data = db_return_history(message)
    for i in range(len(data['history'])):
        answer += "time - {0:.0f} click - {1}\n".format(data['history'][i]['time'],data['history'][i]['click'])
    return answer

def info_player(value):
    answer = ''
    connection = get_connection()
    data = get_player(connection,value)

    answer += "Country Of Birth: {0}\nDate Of Birth: {1}\nFirst Name: {2}\nName: {3}\nPosition: {4}\nShirt Number: {5}".format(data['countryOfBirth'],
                                                                                                                                data['dateOfBirth'],
                                                                                                                                data['name'],
                                                                                                                                data['nationality'],
                                                                                                                                data['position'],
                                                                                                                                data['shirtNumber'])
    return answer
