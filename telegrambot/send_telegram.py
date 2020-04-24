#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os.path
import os
import sys

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Bot

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def main():
    if not os.path.exists("/tmp/chat_id"):
#    if os.environ.get('TELEGRAM_CHAT_ID') is None or os.environ['TELEGRAM_CHAT_ID']=="":
        print("No chat_id available - make sure receive_telegram.py is running and at a user has interacted with it already. You can also pass a TELEGRAM_CHAT_ID environment variable at startup.")
        sys.exit(2)
    elif len(sys.argv) != 2:
        print("Usage: send_telegram.py TEXTMESSAGE")
        sys.exit(1)
    else:
        chat_id_file = open("/tmp/chat_id", "r")
        chat_id = chat_id_file.read()
        chat_id_file.close()
        Bot(os.environ['TELEGRAM_BOT_ID']).send_message(chat_id, sys.argv[1])

if __name__ == '__main__':
    main()
