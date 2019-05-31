from pymongo import MongoClient
import config
import json
import pprint

client = MongoClient(config.exch_name_host, config.exch_host)

db = client[config.exch_name_bd]
users = db[config.exch_name_collections[0]]

def db_add_user(info):
    users.insert_one(info)

def db_return_user(message):
    chat_id = message.chat.id

    user = users.find_one({'chat_id':chat_id})
    return user

def db_update_state(message,menu):
    chat_id = message.chat.id
    users.update_one({'chat_id':chat_id},{'$set':{'state':menu}})

def db_update_history(message,action):
    chat_id = message.chat.id
    users.update_one({'chat_id':chat_id},{'$push':{'history':{'time':action[0],'click':action[1]}}})

def db_return_history(message):
    chat_id = message.chat.id

    data = users.find_one({'chat_id':chat_id})
    return data
