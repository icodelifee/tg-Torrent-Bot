const config = require("../config");
const telebot = require("telebot");
const bot = new telebot(config.botToken);
const parseMode = config.parseMode;

const start = (msg) => {
  let replyMarkup = bot.inlineKeyboard([
    [
      bot.inlineButton("Support Chat", { url: "t.me/itorrentsupportchat" }),
      bot.inlineButton("Android App", {
        url:
          "https://play.google.com/store/apps/details?id=com.icodelife.itorrentsearch",
      }),
    ],
  ]);
  const startText = `<b>Hi, I Can Search Torrent Database For Your Query.</b>\nUse Command /find To Search\neg: /find ubuntu`;
  bot.sendMessage(msg.chat.id, startText, { parseMode, replyMarkup });
};
module.exports = start;
