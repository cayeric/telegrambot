#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os.path
import os
import sys
from select import select

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
    chat_id_file = open("/tmp/chat_id", "r")
    chat_id = chat_id_file.read()
    chat_id_file.close()

    # read message from source depending on given arguments
    if len(sys.argv) == 3 and sys.argv[1]=="-f":
        # read message from file, but truncate to 4000 chars
        msg_file = open(sys.argv[2], "r")
        message = msg_file.read()
        msg_file.close()
    elif len(sys.argv) == 2 and sys.argv[1]=="-i":
        # read message from stdin
        rlist, _, _ = select([sys.stdin], [], [], 3)
        if rlist:
            message = sys.stdin.readline()
        else:
            print ("No input. Abort.")
            sys.exit(2)
    elif len(sys.argv) == 3 and sys.argv[1]=="-t":
        message=sys.argv[2]
    else:
        print("Usage: send_telegram.py -t TEXTMESSAGE | -f MESSAGEFILE | -i")
        sys.exit(1)

    if len(message) > 4000:
        message = message[:4000]+"... truncated"

    print("I'd like to send out: " + message)
    Bot(os.environ['TELEGRAM_BOT_ID']).send_message(chat_id, message)

if __name__ == '__main__':
    main()
