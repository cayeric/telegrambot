#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import os
import base64
import random, string

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

incoming_messages_folder="/var/telegrambot/messages"

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

#if len(sys.argv) != 3 and len(sys.argv) != 2:
#    print("Usage: receive_telegram.py BOT_ID [HOOK_PATH]")
#    print("  if no HOOK_PATH available, incoming mesage gets dispatched to stdout unencoded")
#    print("   otherwise the hook gets calle with the base64-encoded message text")
#    sys.exit(1)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
    chat_id = open("/tmp/chat_id", "w")
    chat_id.write(str(update.message.chat.id))
    chat_id.close()

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    # update.message.reply_text(update.message.text)
    chat_id = open("/tmp/chat_id", "w")
    chat_id.write(str(update.message.chat.id))
    chat_id.close()
#    os.environ['TELEGRAM_CHAT_ID']=str(update.message.chat.id)
#    if len(sys.argv) == 2:
    msg_name=randomword(12)+".msg"
    msg_file=open("/"+msg_name, "w")
    msg_file.write(update.message.text)
    msg_file.close()
    os.system("mv /"+msg_name+" "+incoming_messages_folder)
#        print(update.message.text)
#    else:
#        text = base64.b64encode(update.message.text.encode()).decode()
#        os.system(sys.argv[2]+" \'"+text+"\'")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    if os.environ.get('TELEGRAM_BOT_ID') is None:
        print("TELEGRAM_BOT_ID environment variable missing - abort")
        sys.exit(1)
    updater = Updater(os.environ['TELEGRAM_BOT_ID'], use_context=True)

    if os.environ.get('TELEGRAM_CHAT_ID') is not None:
        chat_id = open("/tmp/chat_id", "w")
        chat_id.write(str(os.environ['TELEGRAM_CHAT_ID']))
        chat_id.close()

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
