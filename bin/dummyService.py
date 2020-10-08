# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 17:08:08 2020

@author: hp
"""

import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/index',methods=['GET'])
def checkStatus():
    return "YAY!!! its working"


@app.route('/add',methods=['GET'])
def addNum():
    a = 2
    b = 3
    return "The sm of {} and {} is {}".format(a,b,a+b)


app.run(host='localhost',port=8023)