from flask import Flask
from datetime import datetime
import os
import redis

r = redis.from_url(os.environ.get("REDIS_URL"))

app = Flask(__name__)

@app.route('/')
def homepage():
    now = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    previous = r.get('time')
    r.set('time', now)

    return f"""
    <h1>Hello heroku</h1>
    <p>It is currently {now}.</p>
    <p>Previous time was: {previous}.</p>
    """

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

