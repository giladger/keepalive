from flask import Flask
import time
import os
import redis
from telegram import Bot

r = redis.from_url(os.environ.get("REDIS_URL"))
telegram = Bot(os.environ.get("TELEGRAM_BOT_TOKEN"))

app = Flask(__name__)

@app.route('/')
def homepage():
    now = time.time()
    previous = r.get('connection_time')
    r.set('connection_time', now)
    telegram.send_message(os.environ.get("TELEGRAM_USER_ID"), f"Hello! {now}")

    return ""

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

