from flask import Flask,render_template
from  fetch_pred import get_pred_eth,get_pred_btc ,get_pred_doge,get_pred_shib
import os

from pathlib import Path
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/currency_details/<int:id>')
def currency_details(id):
    if id==1:
        output = get_pred_btc()
        fig = output[0]
        my_file = Path("static/btc-pred.png")
        if my_file.is_file():
            print('**********  file Exist    deleting file')
            os.remove(my_file)
        fig.get_figure().savefig('static/btc-pred.png')
        data = [(str(output[2][i])[0:10],output[1][i]) for i in range(0,len(output[1]))]
        return render_template('details.html' , img =1,data=data)
    elif id==2:
        output = get_pred_doge()
        fig = output[0]
        
        my_file = Path("static/doge-pred.png")
        if my_file.is_file():
            print('**********  file Exist    deleting file')
            os.remove(my_file)
        fig.get_figure().savefig('static/doge-pred.png')
        data = [(str(output[2][i])[0:10],output[1][i]) for i in range(0,len(output[1]))]
        return render_template('details.html' , img =2,data=data)
    elif id==3:
        output = get_pred_eth()
        fig = output[0]
        my_file = Path("static/eth-pred.png")
        if my_file.is_file():
            print('**********  file Exist    deleting file')
            os.remove(my_file)
        fig.get_figure().savefig('static/eth-pred.png')
        data = [(str(output[2][i])[0:10],output[1][i]) for i in range(0,len(output[1]))]
        return render_template('details.html' , img =3,data=data)
    elif id==4:
        output = get_pred_shib()
        fig = output[0]
        my_file = Path("static/shib-pred.png")
        if my_file.is_file():
            print('**********  file Exist    deleting file')
            os.remove(my_file)
        fig.get_figure().savefig('static/shib-pred.png')
        data = [(str(output[2][i])[0:10],output[1][i]) for i in range(0,len(output[1]))]
        return render_template('details.html' , img =4,data=data)
    else:
       return "Wrong Input Received"


app.run(debug=True)  