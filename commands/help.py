from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import config


def help(bot, update):
    chat_id = update.message.chat.id
    keyboard = [[
        InlineKeyboardButton('Support Chat',
                             url=config.supportChatUrl)
    ],
        [
            InlineKeyboardButton('Android App Link',
                                 url=config.appUrl)
        ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.sendMessage(chat_id, "*You Have Requested For Help!*\n"
                             "<b>Available commands are: </b>\n" +
                    "-/find - <code>Searches Torrent Database</code>\n"
                    "Ask/Report In Support Group If You Have Any Problem With This Bot.Kthnxbye",
                    parse_mode='HTML',
                    reply_markup=reply_markup)

