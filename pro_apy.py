from flask import Flask, jsonify, request, abort
import pymongo
import json
import requests
import jwt
import time
from datetime import datetime, timedelta
from functools import wraps
import AdminMenu

application = Flask(__name__)


@app.route('/')
def root():
    return'API levantada'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["proyecto"]
tabla = mydb["Usuarios"]

def comprobar_admin():
    query = {'user': User, 'pass': password}
   projection = {'is_admin': 1}
   result = mydb.Usuarios.find_one(query, projection)

@application.route('/login', methods=['GET'])
def get_posts():
    comprobar_admin()
   if():
      menu_loged()


































if __name__ == '__main__':
    application.run(debug=True)

