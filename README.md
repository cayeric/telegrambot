* Telegram overview about bots: [documentation](https://core.telegram.org/bots)
* Python telegram bot wrapper: [documentation](https://python-telegram-bot.readthedocs.io/en/stable/index.html) / [github](https://github.com/python-telegram-bot/python-telegram-bot)

How to create a bot
-------------------
1. use botfather to create a bot, he’ll return the Bot ID which is needed to connect to the bot.
2. build and run the container on docker host
3. to receive messages, start the *receive_telegram.py* script, pass **bot_id** and **hook script** as arguments. When a telegram arrives the hook script gets called with the base64 encoded text message. The chat id will be recorded for outgoing messages. If no hook was passed as argument, the incoming message will be printed to stdout.
4. To send a telegram, call *send_telegram.py* with the **message text** as argument. This is only possible if at least one telegram was previously received (and the chat_id recorded from this message).