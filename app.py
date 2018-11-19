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
import pyodbc
#import plotly
app = Flask(__name__)




def connect_mysql():

    driver = '/usr/local/lib/libmsodbcsql.13.dylib'
    driver = '{ODBC Driver 13 for SQL Server}'
    
    cnxn = pyodbc.connect(
                            "Server=shoesclothing.net;"
                            "Database=Gez_pruebas;"
                            "uid=gezsa001;pwd=gez9105ru2")
    
    
    df = pd.read_sql_query('select TOP 5 * from mov_vtasdevcli', cnxn)
    
    print(df.head())
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
    
   # connect_mysql()   
    
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
                           message = os.system('ls'),
                           message2 = os.system('ls ../'),
                           message3 = os.system('ls ../../'),
                           velocity_max = 1)



if __name__ == "__main__":
    app.run()

