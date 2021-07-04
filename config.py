import os

TOKEN = os.environ.get('1854010658:AAG7mV47VuzxCu0QS7d_JOgsIOF7I_qja1o')

WEBHOOK_HOST = "hlwrld-bot.herokuapp.com"
WEBHOOK_PORT = int(os.environ.get('PORT', '80'))
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_URL_BASE = "https://{}".format(WEBHOOK_HOST)
WEBHOOK_URL_PATH = "/{}/".format(TOKEN)
//67578
