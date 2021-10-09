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
        fig = get_pred_btc()
        my_file = Path("static/btc-pred.png")
        if my_file.is_file():
            print('**********  file Exist    deleting file')
            os.remove(my_file)
        fig.get_figure().savefig('static/btc-pred.png')
        return render_template('details.html' , img =1)
    elif id==2:
        fig = get_pred_doge()
        my_file = Path("static/doge-pred.png")
        if my_file.is_file():
            print('**********  file Exist    deleting file')
            os.remove(my_file)
        fig.get_figure().savefig('static/doge-pred.png')
        return render_template('details.html' , img =2)
    elif id==3:
        fig =get_pred_eth()
        my_file = Path("static/eth-pred.png")
        if my_file.is_file():
            print('**********  file Exist    deleting file')
            os.remove(my_file)
        fig.get_figure().savefig('static/eth-pred.png')
        return render_template('details.html' , img =3)
    elif id==4:
        fig =get_pred_shib()
        my_file = Path("static/shib-pred.png")
        if my_file.is_file():
            print('**********  file Exist    deleting file')
            os.remove(my_file)
        fig.get_figure().savefig('static/shib-pred.png')
        return render_template('details.html' , img =4)
    else:
       return "Wrong Input Received"


app.run(debug=True)  