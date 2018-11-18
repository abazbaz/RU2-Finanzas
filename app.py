#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:23:52 2018

@author: abazbaz
"""

from flask import Flask, render_template, jsonify, request, redirect, make_response, url_for
import pandas as pd
import numpy as np
import os
import MySQLdb 
app = Flask(__name__)




def connect_mysql():
    db = MySQLdb.connect(host="shoesclothing.net",user="gezsa001",
                  passwd="gez9105ru2",db="Gez_pruebas")
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    
    # Create table as per requirement
    sql = """CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )"""

    cursor.execute(sql)
    
    db.close()
    return


@app.route('/', methods=['GET', 'POST'])
def index():
    vendor = list(['Gosh','Caterpillar','Flexi'])
    expense_category = list(['bazbaz','adrian'])
    expense_sub_category = list(['a','ab','gg'])
    
    
    
#    vendor = ['Agregar Nuevo Provedor'] + vendor
#    expense_category = ['Agregar Nueva Categoria','Una categoria muuy muuy muuy muuy muuy muuy muuy larga'] + expense_category
#    expense_sub_category = ['Agregar Nueva Sub-categoria'] + expense_sub_category
    
    
    return render_template("navbar.html",
                           navbar_data_capture = 'active',
                           title = "Captura de Gastos",
                           expense_category = expense_category,
                           expense_sub_category = expense_sub_category,
                           vendor = vendor,
                           velocity_max = 1)
    
    
@app.route('/data_capture', methods=['GET', 'POST'])

def data_capture():
    
    connect_mysql()
    vendor = list(['Gosh','Caterpillar','Flexi'])
    expense_category = list(['bazbaz','adrian'])
    expense_sub_category = list(['a','ab','gg'])
    
#    vendor = ['Agregar Nuevo Provedor'] + vendor
#    expense_category = ['Agregar Nueva Categoria','Una categoria muuy muuy muuy muuy muuy muuy muuy larga'] + expense_category
#    expense_sub_category = ['Agregar Nueva Sub-categoria'] + expense_sub_category
    
    user_inputs = dict(request.form)
    print(user_inputs)
    
    return render_template("data_capture.html",
                           navbar_data_capture = 'active',
                           title = "Captura de Gastos",
                           expense_category = expense_category,
                           expense_sub_category = expense_sub_category,
                           vendor = vendor,
                           velocity_max = 1)



if __name__ == "__main__":
    app.run()

