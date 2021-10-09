'''
Flask as GIU to present model outputs in better way
'''

from flask import Flask,render_template
from  fetch_pred import get_pred_eth,get_pred_btc ,get_pred_doge,get_pred_shib  # self-defined funstion to get data that need to be presented on web-pages
import os  # for file manupilation

from pathlib import Path  # for file manupilation
#  creating Flask App
app = Flask(__name__)

#  Main Index Page
@app.route('/')
def home():
    '''
    provides user interface to select which crypto prection user want to see
    '''
    return render_template('home.html')


@app.route('/currency_details/<int:id>')
def currency_details(id):
    '''
    Argumennt:
            id : int input , dont need to provide manually , directly taken if user select any of crypto from home.html
    Return :
            Web page conating Appropriate Image And Table values of predicted data accoring to ID Values
    '''
    if id==1:  # for Bitcoin
        output = get_pred_btc()  # get prediction graph and value from fetch_pred.py
        fig = output[0]   # 1st retrun a plot conating prediction values
        my_file = Path("static/btc-pred.png")  # path where png file will be stored
        if my_file.is_file():  # deleting previous file if exist
            os.remove(my_file)
        fig.get_figure().savefig('static/btc-pred.png')   # getting plot figure and saving it in mentioned path  
        data = [(str(output[2][i])[0:10],output[1][i]) for i in range(0,len(output[1]))]  # for displaying prediction values in the form of table
        return render_template('details.html' , img =1,data=data)  # rendering html file with correspong btc data
    elif id==2:  # for DogeCoin
        ''' same working as above '''
        output = get_pred_doge()
        fig = output[0]
        my_file = Path("static/doge-pred.png")
        if my_file.is_file():
            os.remove(my_file)
        fig.get_figure().savefig('static/doge-pred.png')
        data = [(str(output[2][i])[0:10],output[1][i]) for i in range(0,len(output[1]))]
        return render_template('details.html' , img =2,data=data)
    elif id==3:  # for Etherum
        ''' same working as above '''
        output = get_pred_eth()
        fig = output[0]
        my_file = Path("static/eth-pred.png")
        if my_file.is_file():
            os.remove(my_file)
        fig.get_figure().savefig('static/eth-pred.png')
        data = [(str(output[2][i])[0:10],output[1][i]) for i in range(0,len(output[1]))]
        return render_template('details.html' , img =3,data=data)
    elif id==4: # For Shiba-Inu Coin
        ''' same working as above '''
        output = get_pred_shib()
        fig = output[0]
        my_file = Path("static/shib-pred.png")
        if my_file.is_file():
            os.remove(my_file)
        fig.get_figure().savefig('static/shib-pred.png')
        data = [(str(output[2][i])[0:10],output[1][i]) for i in range(0,len(output[1]))]
        return render_template('details.html' , img =4,data=data)
    else:
        #  for safer side if user hits the url with wrong id
       return "Wrong Input Received , please Go back and select Appropriate Crypto Values"


# app.run(debug=True)   # Running app 
app.run()