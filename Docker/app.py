from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'

@app.route('/hello/')
def hello_world():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> todo"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'Why Hello %s!\n' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)     # open for everyone
