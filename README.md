* Telegram overview about bots: [documentation](https://core.telegram.org/bots)
* Python telegram bot wrapper: [documentation](https://python-telegram-bot.readthedocs.io/en/stable/index.html) / [github](https://github.com/python-telegram-bot/python-telegram-bot)

How to create a bot
-------------------
1. use botfather to create a bot, he’ll return the Bot ID which is needed to connect to the bot.
2. build and run the container on docker host
3. to receive messages, start the *receive_telegram.py* script, pass **bot_id** and **hook script** as arguments. When a telegram arrives the hook script gets called with the base64 encoded text message. The chat id will be recorded for outgoing messages. If no hook was passed as argument, the incoming message will be printed to stdout.
4. To send a telegram, call *send_telegram.py* with the **message text** as argument. This is only possible if at least one telegram was previously received (and the chat_id recorded from this message).

docker command to create a telegram bot that receives and dispatches messages:
docker create --name tele --restart unless-stopped -v /var/messenger/in:/var/telegrambot/messages -e TELEGRAM_BOT_ID="" -e TELEGRAM_CHAT_ID="" telegrambot

dependencies
============
* gforth
* incron

special folders
===============
create a few special folders at installation

* incoming messages: */var/messenger/in*
* outgoing cached messages: */var/messenger/hold*

messenger script
================
* the messenger script can be used as entry point to dispatch messages to the system. it provides a do-not-disturb mode and caches messages for dispatching at a later point in time. the messenger runs as a forth script on **gforth**. to make it available move the script into */usr/local/bin*
* the messenger script expects and reads a messenger config file at */etc/messenger.conf*
* to make sure, that messages are processed even when not invoked manually, call messenger without args per crontab once a day
	$ crontab -e
	* 9 * * * /usr/local/bin/messenger

message_processor script
========================
* incron monitors the incoming folder and invokes the processor script:

	# if root is not allowed, add root to the incron user list:
	$ sudo echo "root" >> /etc/incron.allow

	# edit the incrontab to add the message monitor:
	$ sudo incrontab -e

	# add line:
	/var/messenger/in IN_CLOSE_WRITE /usr/local/bin/message_processor $@/$#

