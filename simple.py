#-*- coding: utf-8 -*-

import os
from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit
from time import sleep

from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
import win32com.client
import sise

app = Flask(__name__)
app.secret_key = "secret"
socketio = SocketIO(app)

user_no = 1

@app.before_request
def before_request():
    global user_no
    if 'session' in session and 'user-id' in session:
        pass
    else:
        session['session'] = os.urandom(24)
        session['username'] = 'user'+str(user_no)
        user_no += 1

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    number1 = str(datetime.now())
    number2 = sise.stock_sise('001')            # KOSPI
    number3 = sise.future_sise('101NC000')      # KOSPI Future
    number4 = sise.stock_sise('201')            # KOSDAQ
    number5 = sise.stock_sise('A005930')        # 삼성전자

    #socketio.emit('newnumber', {'number1': number1, 'number2': number2, 'number3': number3}, namespace='/test')
    emit('newnumber', {'number1': number1, 'number2': number2, 'number3': number3, 'number4': number4, 'number5': number5}, namespace='/test')

    # 환율
    number6 = sise.overseaMarket('99934')          # 달러인텍스(NYBOT)
    number7 = sise.overseaMarket('FX@CNY')         # 중국위한
    number8 = sise.overseaMarket('FX@HKD')        # 홍콜달러
    number9 = sise.overseaMarket('FX@KRW')         # 한국원
    number10 = sise.overseaMarket('FX@JPY')        # 달러인텍스(NYBOT)
    emit('newnumber', {'number6': number6, 'number7': number7, 'number8': number8, 'number9': number9, 'number10': number10}, namespace='/test')

    # CME선물
    number11 = sise.overseaMarket('EDNH')       # E-Mini S&P 500
    number12 = sise.overseaMarket('ENXH')       # E-Mini Nasdaq 100
    emit('newnumber', {'number11': number11, 'number12': number12}, namespace='/test')

    # Global
    number13 = sise.overseaMarket('SHANG')      # 중국상해종합쥐수
    number14 = sise.overseaMarket('CZ#399106')  # 심천종합지수
    number15 = sise.overseaMarket('HK#HS')      # 항셍지수
    number16 = sise.overseaMarket('HSCE')       # 홍콩H지수
    number17 = sise.overseaMarket('JP#NI225')   # 니케이225
    number18 = sise.overseaMarket('JP#TOPIX')   # 일본TOPIX
    number19 = sise.overseaMarket('IN#BOMBAY')  # 인도SENSEX
    emit('newnumber', {'number13': number13, 'number14': number14, 'number14': number14, 'number15': number15, 'number16': number16, 'number17': number17, 'number18': number18, 'number19': number19}, namespace='/test')

    # commodity
    number20 = sise.overseaMarket('95070')      # DRAM Exchange Index
    number21 = sise.overseaMarket('BRENTF')     # Brent 북해산
    number22 = sise.overseaMarket('CM@NGLD')    # 금
    number23 = sise.overseaMarket('99915')      # 구리(NYMEX) 
    emit('newnumber', {'number20': number20, 'number21': number21, 'number22': number22, 'number23': number23}, namespace='/test')

    # 채권
    number24 = sise.overseaMarket('TR@10Y')     # 10년 T-note
    number25 = sise.overseaMarket('TR@30Y')     # 30년 T-note
    number26 = sise.overseaMarket('99925')      # 미국채권 10-year(CBT)
    number27 = sise.overseaMarket('DE@10Y')     # 독일 10년 Bund
    number28 = sise.overseaMarket('DE@30Y')     # 독일 30년 Bund
    emit('newnumber', {'number24': number24, 'number25': number25, 'number26': number26, 'number27': number27, 'number28': number28}, namespace='/test') 


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

@socketio.on("request", namespace='/mynamespace')
def request(message):
    emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80, debug=True)
