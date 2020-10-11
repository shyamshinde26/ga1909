# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 17:34:09 2020

@author: hp
"""

import flask
from flask import Flask, request
from summarizer import SummarizeDoc

app = Flask(__name__)

@app.route('/get_summary',methods=['GET'])
def findSummary():
    summarizeObj = SummarizeDoc()
    summary = summarizeObj.findSummary()
    return summary

app.run('0.0.0.0',80)