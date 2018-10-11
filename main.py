from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater(token='679306216:AAHuQD0_velGKfcN11E4_6eqItvg4zDCNtc') 
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s-%(levelname)s-%(messages)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет! Йо-хо-хо!')
def textMessage(bot,update):
    response = 'Твое сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text = response)
def sticker(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text = 'Не шли мне стикеры, плз(((')


start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
sticker_message_handler = MessageHandler(Filters.sticker, sticker)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(sticker_message_handler)

updater.start_polling(clean=True)

updater.idle()

if __name__ == '__main__':
    main()