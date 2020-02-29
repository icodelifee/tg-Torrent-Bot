

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import config


def start(bot, update):
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
    bot.sendMessage(chat_id, "<b>Hi, I Can Search Torrent Database For Your Query.</b>\n\n"
                             "Supports Inline Mode \n-/help For More Info\n",
                    parse_mode='HTML',
                    reply_markup=reply_markup)
