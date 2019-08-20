from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)


app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'Why Hello %s!\n' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0')     # open for everyone
