import base64
import json
from shutil import move
from uuid import uuid4

from telegram import InlineQueryResultGame

'''
Getting localisation file with games and messages
'''


def getBotSettings():
    with open('bot.json', encoding='UTF-8') as data_file:
        data = json.load(data_file)
    return data


'''
JSON validation
'''


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


'''
Replace localisation file. It uses, when you want to add or remove a game
'''


def replaceSettings(bot, update, filename='bot'):
    settings = getBotSettings()
    if update.message.document:
        move(filename + '.json', filename + '_old' + '.json')
        file_id = update.message.document.file_id
        bot.getFile(file_id).download(filename + '.json')
        with open(filename + '.json', 'r') as content_file:
            if not is_json(content_file.read()):
                move(filename + '_old' + '.json', filename + '.json')
                bot.sendMessage(update.message.chat_id, text=settings['message']['json_bot_not_valid'])
            else:
                bot.sendMessage(update.message.chat_id, text=settings['message']['json_bot_valid'])


'''
Default message /start
'''


def menu(bot, update, id=-1):
    settings = getBotSettings()
    uid = update.message.from_user.id
    if not id == -1:
        uid = id
    bot.sendMessage(uid, text=settings['message']['Play with friends!'])


'''
Checking is admin
'''


def isAdmin(id):
    return id in getBotSettings()['admins']


'''
Get all games for inline query
'''


def inlineGame(bot, update):
    games = getBotSettings()['games']
    query = update.inline_query.query
    inline_games = list()
    for game in games:
        if game['name'].startswith(query):
            inline_games.append(
                InlineQueryResultGame(type='game', id=str(uuid4()),
                                      game_short_name=game['game_short_name']))
    update.inline_query.answer(inline_games)


'''
Sending a localisation file, if user's admin
'''


def editFile(bot, update):
    settings = getBotSettings()
    if isAdmin(update.message.from_user.id):
        uid = update.message.from_user.id
        bot.sendDocument(uid, document=open('bot.json', 'rb'))
    else:
        bot.sendMessage(update.message.chat_id, text=settings['messages']['not_admin'])


'''
Return link, when user's clicking on inline button
'''


def click(bot, update):
    games = getBotSettings()['games']
    for game in games:
        if game['game_short_name'] == update.callback_query.game_short_name:
            # Parameters that will be encoded in Base64 and will be sent as url parameter
            # In this example we're encoding user id and inline message id
            # Those parameters're required for updating user's high score
            parameters = {'u': update.callback_query.from_user.id,
                          'i': update.callback_query.inline_message_id}
            bot.answerCallbackQuery(callback_query_id=update.callback_query.id,
                                    url=game['url'] + '/#player_info={}'.format(
                                        base64.b64encode(json.dumps(parameters).encode('utf-8')).decode("utf-8")))
