#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os.path
import sys

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Bot

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def main():
    if not os.path.exists("/tmp/chat_id"):
        print("No chat_id available - make sure mvpabot.py is running and at a user has interacted with it already")
        sys.exit(1)
    elif len(sys.argv) != 3:
        print("Usage: send_telegram.py BOT_ID TEXTMESSAGE")
        sys.exit(2)
    else:
        chat_id_file = open("/tmp/chat_id", "r")
        chat_id = chat_id_file.read()
        Bot(sys.argv[1]).send_message(chat_id, sys.argv[2])

if __name__ == '__main__':
    main()
