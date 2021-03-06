# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 10:35:17 2020

@author: KSK
"""

from flask import Flask,render_template,url_for,request
import pandas as pd
import pickle

# load the model from the disk

loaded_model=pickle.load(open("data_pick.pkl","rb"))
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    df=pd.read_csv('clean_real_2016_1.csv')
    my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
    my_prediction=my_prediction.tolist()
    return render_template('result.html',prediction=my_prediction)

if __name__=='__main__':
    app.run(debug=True)
