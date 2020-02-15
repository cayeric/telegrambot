FROM alpine
RUN apk add python3 python3-dev gcc g++ libffi-dev openssl-dev
RUN pip3 install python-telegram-bot
COPY receive_telegram.py receive_telegram.py
COPY send_telegram.py send_telegram.py
