const config = require("../config");
const telebot = require("telebot");
const flatCache = require("flat-cache");
const path = require("path");

var cachePath = path.resolve(__dirname, "../cache");
const cache = flatCache.load("itorrent", cachePath);
const bot = new telebot(config.botToken);
const parseMode = config.parseMode;

const callbackhandler = async (msg) => {
  const split = msg.data.split(":");
  const queryKey = split[1];
  if (split[0] === "back") {
    const buttons = [];
    const data = await cache.getKey(queryKey);
    for (var i = 0; i <= 20; i++) {
      const callback = Math.random().toString(36).substring(7) + ":" + queryKey;
      cache.setKey(callback, data[i]);
      buttons.push([
        bot.inlineButton(data[i].name, {
          callback,
        }),
      ]);
    }
    const replyMarkup = bot.inlineKeyboard(buttons);
    cache.save();
    return bot.editMessageText(
      {
        chatId: msg.message.chat.id,
        messageId: msg.message.message_id,
      },
      "<b>🔍Search Query Results:👇</b>\n",
      {
        parseMode,
        replyMarkup,
      }
    );
  } else {
    const data = await cache.getKey(msg.data);
    const replyMarkup = bot.inlineKeyboard([
      [bot.inlineButton("Back ◀️", { callback: `back:${queryKey}` })],
    ]);
    var callback = `<b>${data.name}</b>\n<b>Size </b> : ${data.size} \n<b>🗓Uploaded : </b> ${data.age} Ago \n<b>⬆️</b> ${data.seeder} \n<b>⬇️</b> ${data.leecher} \n<b>🔗Magnet👇: </b>\n<code>${data.magnet} </code>`;
    return bot.editMessageText(
      {
        chatId: msg.message.chat.id,
        messageId: msg.message.message_id,
      },
      callback,
      {
        parseMode,
        replyMarkup,
      }
    );
  }
};

module.exports = callbackhandler;
