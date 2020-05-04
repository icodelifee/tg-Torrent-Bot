const config = require("../config");
const telebot = require("telebot");
const flatCache = require("flat-cache");
const search = require("../utils/api");
const path = require('path')
const bot = new telebot(config.botToken);
const parseMode = config.parseMode;

var cachePath = path.resolve(__dirname, "../cache");
var cache = flatCache.load("itorrent", cachePath);

const find = async (msg, props) => {
  const searchQuery = props.match[1];
  const buttons = [];
  const searchJson = await search(searchQuery);
  if (searchJson.length <= 0) {
    return msg.reply.text("Oops! Couldnt Find Anything");
  }
  const queryKey = Math.random().toString(36).substring(7);
  cache.setKey(queryKey, searchJson);
  for (var i = 0; i <= 20; i++) {
    const callback = Math.random().toString(36).substring(7) + ":" + queryKey;
    cache.setKey(callback, searchJson[i]);
    buttons.push([
      bot.inlineButton(searchJson[i].name, {
        callback,
      }),
    ]);
  }
  const replyMarkup = bot.inlineKeyboard(buttons);
  cache.save(true);
  return bot
    .sendMessage(msg.chat.id, "<b>🔍Search Query Results:👇</b>\n", {
      parseMode,
      replyMarkup,
      notification: true,
      replyToMessage: msg.message_id,
      webPreview: false,
    })
    .catch((err) => console.log(err));
};
module.exports = find;
