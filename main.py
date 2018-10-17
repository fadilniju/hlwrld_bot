
import os
import logging
import ssl
import config

from aiohttp import web

import telebot


#Логирование
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

# Бот
bot = telebot.TeleBot(config.TOKEN)

app = web.Application()

"""
Создаем обработчик запросов от серверов Telegram на
aiohttp-сервер для реализации вебхука
"""
async def handle(request):
    if request.match_info.get('token') == bot.token:                 
        request_body_dict = await request.json()
        update = telebot.types.Update.de_json(request_body_dict)
        bot.process_new_updates([update])
        return web.Response()
    else:
        return web.Response(status=403)

app.router.add_post('/{token}/', handle)


# Хэндлеры
# Обрабатываем '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,
                 ("Hi there, I am EchoBot.\n"
                  "I am here to echo your kind words back to you."))


# Обрабатываем все остальные сообщения
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()

# Set webhook
bot.set_webhook(url=config.WEBHOOK_URL_BASE+config.WEBHOOK_URL_PATH)


# Start aiohttp server
web.run_app(
    app,
    host=config.WEBHOOK_LISTEN,
    port=config.WEBHOOK_PORT,
)    
    
"""
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://hlwrld-bot.herokuapp.com/" + TOKEN)



def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет! Йо-хо-хо!')
def textMessage(bot,update):
    response = 'Твое сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text = response)
def sticker(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text = 'Не шли мне стикеры, плз(((')
    
    

custom_keyboard = [[telegram.KeyboardButton("Option 1")],
                       [telegram.KeyboardButton("Option 2")]]
reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
def get_menu(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
                  text="Custom Keyboard Test", 
                  reply_markup=reply_markup)


start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
sticker_message_handler = MessageHandler(Filters.sticker, sticker)
menu_command_handler = CommandHandler('menu',get_menu)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(sticker_message_handler)
dispatcher.add_handler(menu_command_handler)

updater.start_polling(clean=True)

updater.idle()
"""
