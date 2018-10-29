from pymongo import MongoClient
import config

client = MongoClient(config.DB_URL)

db = config.DB_URL
print (db)
"""
db = db.split('/')[-1]
db_con = client[db]


def get_curr_state(user_id):
    with db_con['user_states'] as users_coll:
        try:
            return users_coll.find_one({"_id": user_id})['state']
        except KeyError:
            return config.States.S_START.value


def set_curr_state(user_id, value):
    with db_con['user_states'] as users_coll:
        try:
            users_coll.insert_one({"_id": user_id, "state": value})
            return True
        except:
            print('An error occured while trying post to db')
            return False
"""