import re

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

from utils.gettorrentsjson import returnResult


def button(bot, update):
    callback_data = int(update.callback_query.data)
    chat_id = update.callback_query.message.chat_id
    msg_id = update.callback_query.message.message_id
    regex = r"(?<=Search Query : ).*$"
    test_str = update.callback_query.message.text
    toSearch = re.search(regex, test_str).group(0)
    cb_json = returnResult(toSearch)
    if len(cb_json) >= 10:
        limit = 10
    else:
        limit = len(cb_json)
    if callback_data != 88:
        back_keyboard = [[
            InlineKeyboardButton('◀️Back', callback_data='88')
        ]]
        reply_markup = InlineKeyboardMarkup(back_keyboard)
        callback_string = f"{cb_json[callback_data]['title']} [{cb_json[callback_data]['size']}]\n" \
                          f"<b>🗓Uploaded : </b> {cb_json[callback_data]['date']}\n" \
                          f"<b>⬆️ </b>{cb_json[callback_data]['seeds']} " \
                          f"<b>⬇️</b> {cb_json[callback_data]['leechs']} \n" \
                          f"<b>🔗Magnet👇: </b>\n <code>{cb_json[callback_data]['magnet']}" \
                          f"</code>\n<b>Search Query : </b>{toSearch}"
        bot.editMessageText(callback_string,
                            chat_id=chat_id,
                            message_id=msg_id,
                            parse_mode='HTML',
                            reply_markup=reply_markup,
                            disable_web_page_preview=True
                            )
    else:
        keyboard = list()
        for i in range(limit):
            keyboard.append([
                InlineKeyboardButton(cb_json[i]['title'],
                                     callback_data=i)
            ])
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.editMessageText("<b>🔍Search Query Results:👇</b>\n"
                            "<pre>Search Query : </pre>" + "<i>" + toSearch + "</i>\n",
                            parse_mode=ParseMode.HTML,
                            chat_id=chat_id,
                            message_id=msg_id,
                            reply_markup=reply_markup)
