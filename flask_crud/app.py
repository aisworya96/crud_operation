from flask import Flask
from flaskext.mysql import MySQL
import pymysql

mysql = MySQL()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()