from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import logging
import telegram

#Логирование
logging.basicConfig(format='%(asctime)s - %(name)s-%(levelname)s-%(messages)s', level=logging.INFO)
logger = logging.getLogger(__name__)

#объявляем бота
PORT = int(os.environ.get('PORT', '8443'))
TOKEN = "679306216:AAHuQD0_velGKfcN11E4_6eqItvg4zDCNtc"
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

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
    
    

custom_keyboard = [['top-left', 'top-right'],
                       ['bottom-left', 'bottom-right']]
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

