#!/usr/bin/python
# -*- coding: utf8 -*-
import joblib
import flask
from flask import render_template, request, jsonify
import numpy as np
import traceback
import pickle
import pandas as pd

# App definition
app = flask.Flask(__name__,template_folder='templates')
 

@app.route('/')
def index():
  return render_template('index.html')

# importing models
with open('finalized_model.pkl', 'rb') as f:
   model = pickle.load (f)
 
# https://dev-gang.ru/article/model-mashinnogo-obuczenija-s-flask-rest-api-relacbm4lo/
@app.route('/predict', methods=['POST'])
def predict():
  if flask.request.method == 'POST':
    try:
          df = pd.read_csv('all_datas.csv')
          print(df)
          model_columns = ['Регион',  'Население Медианная зп (руб)',  '92',  '95',  'ДТП на 100000 чел', 'ДТП с погибшими (на 100000 чел)', 'Уровень безработицы. %',  'Преступность(кол-во на 10000 чел)', 'Продолжительность жизни', 'Прожиточный минимум', 'Качество жизни',  'Индекс привлекательности рабочей силы', 'Социальная ориентированность бюджетов']
          json_ = request.json
          query_ = pd.get_dummies(pd.DataFrame(json_))
          query = query_.reindex(columns = model_columns, fill_value= 0)
          lst_drops = ['92', 'Прожиточный минимум']
          drop_list = ['Регион','Качество жизни']
          target = 'Качество жизни'
          df1 = df.copy(deep = True).drop(lst_drops, axis=1)
          df1 = df1.copy(deep = True).drop(drop_list, axis = 1)
          x_test_scaled = (x_test-np.min(x_test))/(np.max(x_test)-np.min(x_test))
          prediction = list(model.predict(query)*100)
          print (prediction)
          return jsonify({
               "prediction":str(prediction)
           })
 
    except:
          return jsonify({
               "trace": traceback.format_exc()
               })


if __name__ == "__main__":
  app.run(debug = True)