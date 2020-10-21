from bot.token import token
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from telegram.ext import Updater

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def do_start(update, context):

    text = "Привет, я бот."

    update.message.reply_text(text)

def main():

    updater = Updater(token=token,
                      use_context=True)

    dp = updater.dispatcher

    start_handler = CommandHandler("start", do_start)

    dp.add_handler(start_handler)
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":

    main()