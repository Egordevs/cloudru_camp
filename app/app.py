from flask import Flask
import os
import socket
import uuid

app = Flask(__name__)

@app.route('/hostname')
def hostname():
    hostname = os.popen("hostname").read()
    return f"<p>{hostname}</p>"

@app.route('/author')
def author():
    author = os.environ.get('AUTHOR', 'Not exist')
    return f"<p>{author}</p>"

@app.route('/id')
def id():
    uuid_value = os.environ.get('UUID', 'Not exist')
    return f"<p>{uuid_value}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)