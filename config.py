import os
from enum import Enum

TOKEN = os.environ.get('BOT_TOKEN')

WEBHOOK_HOST = "hlwrld-bot.herokuapp.com"
WEBHOOK_PORT = int(os.environ.get('PORT', '80'))
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_URL_BASE = "https://{}".format(WEBHOOK_HOST)
WEBHOOK_URL_PATH = "/{}/".format(TOKEN)

DB_URL = os.environ.get('DATABASE_URL')


class States(Enum):
    S_START = "0"
    S_ENTER_NAME = "1"
    S_ENTER_AGE = "2"
    S_ENTER_PIC = "3"
