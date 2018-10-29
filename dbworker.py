from pymongo import MongoClient
import config

client = MongoClient(config.DB_URL)

db_name = config.DB_URL.split('/')[-1]
print(db_name)
db_con = client[db_name]


def get_curr_state(user_id):
    users_coll = db_con['user_states']
    try:
        return users_coll.find_one({"_id": user_id})['state']
    except BaseException:
        return config.States.S_START.value


def set_curr_state(user_id, value):
    users_coll = db_con['user_states']
    try:
        users_coll.save({"_id": user_id, "state": value})
        return True
    except BaseException:
        print('An error occured while trying post to db')
        return False
