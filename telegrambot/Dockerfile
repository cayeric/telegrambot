FROM alpine
RUN apk add python3 python3-dev gcc g++ libffi-dev openssl-dev && \
    pip3 install python-telegram-bot && \
    mkdir -p /var/telegrambot/messages && \
    apk del python3-dev gcc g++ libffi-dev openssl-dev
COPY receive_telegram.py receive_telegram.py
COPY send_telegram.py send_telegram.py
CMD python3 receive_telegram.py
#COPY telegrambot.py telegrambot.py
