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
    
    
@app.route('/captura_egresos', methods=['GET', 'POST'])

def captura_egresos():
    
    vendor = list(['Gosh','Caterpillar','Flexi'])
    categoria = list(['categoria_1','categoria_2','categoria_3','categoria_4','categoria_5'])
    sub_categoria = list(['sub_categoria_1','sub_categoria_2','sub_categoria_3','sub_categoria_4','sub_categoria_5'])
    forma_pago = list(['forma_pago_1','forma_pago_2','forma_pago_3','forma_pago_4','forma_pago_5'])
    
#    vendor = ['Agregar Nuevo Provedor'] + vendor
#    expense_category = ['Agregar Nueva Categoria','Una categoria muuy muuy muuy muuy muuy muuy muuy larga'] + expense_category
#    expense_sub_category = ['Agregar Nueva Sub-categoria'] + expense_sub_category
    
    print(os.system('ls'))
    print(os.system('ls ../'))
    print(os.system('ls ../../'))

    user_inputs = dict(request.form)
    print(user_inputs)
    
    
    return render_template("captura_egresos.html",
                           navbar_data_capture = 'active',
                           title = "Registro de Egresos",
                           categoria = categoria,
                           sub_categoria = sub_categoria,
                           forma_pago = forma_pago,
                           vendor = vendor,
                           velocity_max = 1)



@app.route('/captura_ingresos', methods=['GET', 'POST'])

def captura_ingresos():
    
    tipo_ingreso = list(['Ventas','Concepto'])
    cuenta = list(['cuenta_1','cuenta_2','cuenta_2','cuenta_4','cuenta_5'])
    centro_de_costo = list(['centro_1','centro_2','sub_centro_3','centro_4','centro_5'])
    forma_pago = list(['forma_pago_1','forma_pago_2','forma_pago_3','forma_pago_4','forma_pago_5'])
    

    user_inputs = dict(request.form)
    print(user_inputs)
    
    
    return render_template("captura_ingresos.html",
                           navbar_captura_ingresos = 'active',
                           title = "Registro de Ingresos",
                           centro_de_costo = centro_de_costo,
                           cuenta = cuenta,
                           forma_pago = forma_pago,
                           tipo_ingreso = tipo_ingreso,
                           velocity_max = 1)
    
@app.route('/nomina', methods=['GET', 'POST'])

def nomina():
    
    tipo_ingreso = list(['Ventas','Concepto'])
    cuenta = list(['cuenta_1','cuenta_2','cuenta_2','cuenta_4','cuenta_5'])
    centro_de_costo = list(['centro_1','centro_2','sub_centro_3','centro_4','centro_5'])
    forma_pago = list(['forma_pago_1','forma_pago_2','forma_pago_3','forma_pago_4','forma_pago_5'])
    

    user_inputs = dict(request.form)
    print(user_inputs)
    
    
    return render_template("captura_ingresos.html",
                           navbar_captura_ingresos = 'active',
                           title = "Nomina",
                           centro_de_costo = centro_de_costo,
                           cuenta = cuenta,
                           forma_pago = forma_pago,
                           tipo_ingreso = tipo_ingreso,
                           velocity_max = 1)


if __name__ == "__main__":
    app.run()

