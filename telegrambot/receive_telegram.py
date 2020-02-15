#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import os
import base64

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

if len(sys.argv) != 3 and len(sys.argv) != 2:
    print("Usage: receive_telegram.py BOT_ID [HOOK_PATH]")
    print("  if no HOOK_PATH available, incoming mesage gets dispatched to stdout unencoded")
    print("   otherwise the hook gets calle with the base64-encoded message text")
    sys.exit(1)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
    chat_id = open("/tmp/chat_id", "w")
    chat_id.write(str(update.message.chat.id))

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    # update.message.reply_text(update.message.text)
    chat_id = open("/tmp/chat_id", "w")
    chat_id.write(str(update.message.chat.id))
    if len(sys.argv) == 2:
        print(update.message.text)
    else:
        text = base64.b64encode(update.message.text.encode()).decode()
        os.system(sys.argv[2]+" \'"+text+"\'")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(sys.argv[1], use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
