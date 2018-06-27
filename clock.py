from apscheduler.schedulers.blocking import BlockingScheduler
import time
import os
import redis
from telegram import Bot

r = redis.from_url(os.environ.get("REDIS_URL"))
telegram = Bot(os.environ.get("TELEGRAM_BOT_TOKEN"))

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    now = time.time()
    last_connection = r.get('connection_time')
    if not last_connection:
        return
    
    last_connection = int(last_connection)
    if now - last_connection > 60:
        if r.get('is_connected'):
            r.set('is_connected', False)
            telegram.send_message(os.environ.get("TELEGRAM_USER_ID"), 'No connection')

sched.start()
