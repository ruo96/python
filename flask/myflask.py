from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'
host = '127.0.0.1'
port = 9999

if __name__ == '__main__':
    app.debug = True
    app.run(host, port)