

import logging
import config

from aiohttp import web

import telebot
import dbworker

#Логирование

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

# Бот
bot = telebot.TeleBot(config.TOKEN)

# Вызываем объект App для инициализации http сервера

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
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 ("Привет, я EchoBot.\n"
                  "Я здесь чтобы пересылать твои сообщения.\n"
                  "Как тебя зовут?"))
    dbworker.set_curr_state(message.chat.id, config.States.S_ENTER_NAME.value)
    
@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Что ж, начнём по-новой. Как тебя зовут?")
    dbworker.set_curr_state(message.chat.id, config.States.S_ENTER_NAME.value)


@bot.message_handler(func=lambda message: dbworker.get_curr_state(message.chat.id) == config.States.S_ENTER_NAME.value)
def user_entering_name(message):
    # В случае с именем не будем ничего проверять, пусть хоть "25671", хоть Евкакий
    bot.send_message(message.chat.id, "Отличное имя, запомню! Теперь укажи, пожалуйста, свой возраст.")
    dbworker.set_curr_state(message.chat.id, config.States.S_ENTER_AGE.value)
    
@bot.message_handler(func=lambda message: dbworker.get_curr_state(message.chat.id) == config.States.S_ENTER_AGE.value)
def user_entering_age(message):
    # А вот тут сделаем проверку
    if not message.text.isdigit():
        # Состояние не меняем, поэтому только выводим сообщение об ошибке и ждём дальше
        bot.send_message(message.chat.id, "Что-то не так, попробуй ещё раз!")
        return
    # На данном этапе мы уверены, что message.text можно преобразовать в число, поэтому ничем не рискуем
    if int(message.text) < 5 or int(message.text) > 100:
        bot.send_message(message.chat.id, "Какой-то странный возраст. Не верю! Отвечай честно.")
        return
    else:
        # Возраст введён корректно, можно идти дальше
        bot.send_message(message.chat.id, "Когда-то и мне было столько лет...эх... Впрочем, не будем отвлекаться. "
                                          "Отправь мне какую-нибудь фотографию.")
        dbworker.set_curr_state(message.chat.id, config.States.S_ENTER_PIC.value)   

@bot.message_handler(content_types=["photo"],
                     func=lambda message: dbworker.get_curr_state(message.chat.id) == config.States.S_ENTER_PIC.value)
def user_sending_photo(message):
    # То, что это фотография, мы уже проверили в хэндлере, никаких дополнительных действий не нужно.
    bot.send_message(message.chat.id, "Отлично! Больше от тебя ничего не требуется. Если захочешь пообщаться снова - "
                     "отправь команду /start.")
    dbworker.set_curr_state(message.chat.id, config.States.S_START.value)
    

"""
# Обрабатываем все остальные сообщения (????)
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)
"""

# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()

# Set webhook
bot.set_webhook(url=config.WEBHOOK_URL_BASE+config.WEBHOOK_URL_PATH)


# Start aiohttp server
web.run_app(
    app,
    host=config.WEBHOOK_LISTEN,
    port=config.WEBHOOK_PORT
)    
