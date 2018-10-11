"""
Updater - постоянно извлекает новые обновления из ТГ и передает их в класс Dispatcher
Dispatcher - класс отправляет все виды обновлений зарегистрированным обработчикам(Handler).
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater(token='679306216:AAHuQD0_velGKfcN11E4_6eqItvg4zDCNtc') # Токен API к Телеграм
dispatcher = updater.dispatcher

# Логирование
import logging
logging.basicConfig(format='%(asctime)s - %(name)s-%(levelname)s-%(messages)s', level=logging.INFO)

#Функции обработки команд и сообщений из ТГ
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет! Йо-хо-хо!')
def textMessage(bot,update):
    response = 'Твое сообщение: ' + update.message.text
    bot.send_message(chat_id=udate.message.chat_id, text = response)

#Хэндлеры
start_commnd_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text)

#Регистрируем хэндлеры в диспатчере (Dispatcher)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()