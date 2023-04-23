from flask import render_template,Flask, request
import tkinter as tk
import pandas as pd
from PIL import Image, ImageTk
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.ensemble import *
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import metrics



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
# 사용자 입력값 받기
def result():
    if request.method == 'POST':
        data1 = pd.read_csv('fianl.csv')
        
        data = data1.drop('OutletSales',axis=1)
        target = data1['OutletSales']
        X_train,X_test,y_train,y_test=train_test_split(data,target,test_size=0.2,random_state=2)

        model = LinearRegression()
        model.fit(X_train,y_train)
        pred_y = model.predict(X_test)
        r2 = metrics.r2_score(y_test,pred_y)
        print('R2 : ', (r2,1))
        model.fit(data, target)
        return render_template('result.html',pred = r2)
    

if __name__ == '__main__':
    app.run(debug=True)

