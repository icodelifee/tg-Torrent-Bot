const telebot = require("telebot");
const config = require("./config");
const start = require("./commands/start");
const find = require("./commands/find");
const commandHandler = require("./commands/callbackquery");
const bot = new telebot(config.botToken);

bot.on("/start", start);

bot.on(/^\/find (.+)$/, find);

bot.on("callbackQuery", commandHandler);

bot.start();
