import logging

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

import config
from commands import start
from commands.find import search_query
from commands.buttonhandler import button

def main():
    updater = Updater(config.botToken)
    dp = updater.dispatcher

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    logger = logging.getLogger(__name__)

    dp.add_handler(CommandHandler('find', search_query, pass_args=True))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    logger.info('Listening humans as %s..' % updater.bot.username)
    updater.idle()
    logger.info('Bot stopped gracefully')


def error(update, context):
    """Log Errors caused by Updates."""
    logger = logging.getLogger(__name__)
    logger.warning('Update "%s" caused error "%s"', update, context.error)


if __name__ == '__main__':
    main()
