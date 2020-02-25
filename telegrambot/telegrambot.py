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
hook = None
hook_args = None

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
    chat_id = open("/tmp/chat_id", "w")
    chat_id.write(str(update.message.chat.id))

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('I cannot help you (yet!)')

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

def start(bot_id, hook, hook_args):
    updater = Updater(bot_id, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()
