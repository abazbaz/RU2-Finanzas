#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:23:52 2018

@author: abazbaz
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    return 'OK'

if __name__ == "__main__":
    app.run()

