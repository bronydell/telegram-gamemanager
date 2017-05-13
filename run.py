import json
import logging

from telegram.ext import Updater, CommandHandler, InlineQueryHandler, CallbackQueryHandler, MessageHandler, Filters

import actions

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

with open('bot.json', encoding='UTF-8') as data_file:
    key = json.load(data_file)['key']


def error_callback(bot, update, error):
    print(error)


updater = Updater(key)
updater.dispatcher.add_error_handler(error_callback)
updater.dispatcher.add_handler(CallbackQueryHandler(actions.click))
updater.dispatcher.add_handler(CommandHandler('start', actions.menu))
# Use /getsettings in private messages with bot to get game and admin list
updater.dispatcher.add_handler(CommandHandler('getsettings', actions.editFile))
# Send document to update game list or add/remove admin
updater.dispatcher.add_handler(MessageHandler(Filters.document, actions.replaceSettings))
updater.dispatcher.add_handler(InlineQueryHandler(actions.inlineGame))
updater.start_polling()
updater.idle()
