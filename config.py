import os

TOKEN = os.environ.get('BOT_TOKEN')

WEBHOOK_HOST = "hlwrld-bot.herokuapp.com"
WEBHOOK_PORT = int(os.environ.get('PORT', '80'))
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_URL_BASE = "https://{}".format(WEBHOOK_HOST)
WEBHOOK_URL_PATH = "/{}/".format(TOKEN)