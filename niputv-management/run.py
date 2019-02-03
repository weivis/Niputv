__author__ = 'Ran'
#!bin/python3.6
from app import app, blueprint

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8005, debug=True, threaded=True)