from pymongo import MongoClient
import config

client = MongoClient(config.DB_URL)

db_uri = config.DB_URL.split('/')[-1]
db_con = client[db_uri]


def get_curr_state(user_id):
    users_coll = db_con['user_states']
    try:
        return users_coll.find_one({"_id": user_id})['state']
    except KeyError:
        return config.States.S_START.value


def set_curr_state(user_id, value):
    users_coll = db_con['user_states']
    try:
        users_coll.insert_one({"_id": user_id, "state": value})
        return True
    except:
        print('An error occured while trying post to db')
        return False
