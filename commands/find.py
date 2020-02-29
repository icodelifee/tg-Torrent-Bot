from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from utils.gettorrentsjson import returnResult


def search_query(bot, update, args):
    search_query = ' '.join(args)
    chat_id = update.message.chat.id
    message_id = update.message.message_id
    json = returnResult(search_query)
    if len(json) == 0:
        bot.sendSticker(chat_id, 'CAADBQADYQADZ7RFFii2rILMAAG4cQI',
                        reply_to_message_id=update.message.message_id)
        return
    query_data = ""
    keyboard = list()
    if len(json) >= 20:
        limit = 20
    else:
        limit = len(json)
    for i in range(limit):
        keyboard.append([
            InlineKeyboardButton(json[i]['title'],
                                 callback_data=i)
        ])

    reply_markup = InlineKeyboardMarkup(keyboard)
    message = bot.sendMessage(chat_id, "<b>🔍Search Query Results:👇</b>\n"
                                       "<pre>Search Query : </pre>" + "<i>" + search_query + "</i>\n",
                              parse_mode='HTML',
                              reply_markup=reply_markup,
                              reply_to_message_id=update.message.message_id,
                              disable_web_page_preview=True)
