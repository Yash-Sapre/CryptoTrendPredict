
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from fetch_data import fetch_data
from pickle import load

btc_model =tf.keras.models.load_model('ReqFiles/LSTM_V2_BTC.h5')
eth_model = tf.keras.models.load_model('ReqFiles/LSTM_V2_ETH.h5')
doge_model= tf.keras.models.load_model('ReqFiles/LSTM_V2_DOGE.h5')
shib_model= tf.keras.models.load_model('ReqFiles/LSTM_V2_SHIB.h5')

n_past = 10

def get_pred_btc():
    """
    for getting prediction on future 10 days from today on bitcoin
    args:
            NO Argument Required
    returns :
            {matplolib.plot}: contains graph of actual data and model predicted values  
    
    """
    model = btc_model
    scaler = load(open('ReqFiles/scaler_btc.pkl', 'rb'))
    df=fetch_data(20 ,tickers='BTC-USD')
    data =df['Close']
    init_date = df["Date"][0]
    data = np.array(data)
    data1= data[:10]
    data_scaled = data1.reshape((n_past,1))

    data_scaled = scaler.transform(data_scaled).tolist()
    out_data = []
    i=0
    ran = len(data)-5
    while(i<ran):
        x_input=data_scaled[len(data_scaled)-n_past:]

        x_input=np.array(x_input).reshape((1,n_past,1))
        y_pred = model.predict(x_input)[0][0]
 
        actual_p =scaler.inverse_transform([[y_pred]]).tolist()
        out_data.append(actual_p[0][0])
        data_scaled.append([y_pred])
        i=i+1
    plt.figure(figsize=(20,10))
    datelist = pd.date_range(init_date , periods=len(data)+i-1)
    ax=sns.lineplot(datelist[:len(data)],data, label='Actual_Values', marker='o')
    ax=sns.lineplot(datelist[10:len(data)+5],out_data ,label='Predicted_Values', marker='o')
    ax.set_ylabel('Bitcoin Price in USD')
    ax.set_xlabel('Dates')
    plt.title(f"Bitcoin Price Prediction for Data of Days :{len(data)-5}")
    return (ax,out_data,datelist[10:len(data)+5])

def get_pred_eth():
    """
    for getting prediction on future 10 days from today on Etherum
    args:
            NO Argument Required
    returns :
            {matplolib.plot}: contains graph of actual data and model predicted values  
    
    """
    model = eth_model
    scaler = load(open('ReqFiles/scaler_eth.pkl', 'rb'))
    df=fetch_data(30,tickers='ETH-USD')
    data =df['Close']
    init_date = df["Date"][0]
    data = np.array(data)
    data1= data[len(data)-10:]
    input_data =data1
    data_scaled = data1.reshape((n_past,1))

    data_scaled = scaler.transform(data_scaled).tolist()
    out_data = []
    i=0
    ran = len(data)-5
    while(i<ran):
        x_input=data_scaled[len(data_scaled)-n_past:]

        x_input=np.array(x_input).reshape((1,n_past,1))
        y_pred = model.predict(x_input)[0][0]
 
        actual_p =scaler.inverse_transform([[y_pred]]).tolist()
        out_data.append(actual_p[0][0])
        data_scaled.append([y_pred])
        i=i+1
    plt.figure(figsize=(20,10))
    datelist = pd.date_range(init_date , periods=len(data)+i-1)
    ax=sns.lineplot(datelist[:len(data)],data, label='Actual_Values', marker='o')
    ax=sns.lineplot(datelist[10:len(data)+5],out_data ,label='Predicted_Values', marker='o')
    ax.set_ylabel('Etherum Price in USD')
    ax.set_xlabel('Dates')
    plt.title(f"Etherum Price Prediction for Data of Days :{len(data)-5}")
    return (ax,out_data,datelist[10:len(data)+5])

def get_pred_doge():
    """
    for getting prediction on future 10 days from today on Doge
    args:
            NO Argument Required
    returns :
            {matplolib.plot}: contains graph of actual data and model predicted values  
    
    """
    model = doge_model
    scaler = load(open('ReqFiles/scaler_doge.pkl', 'rb'))
    df=fetch_data(20,tickers='DOGE-USD')
    data =df['Close']
    init_date = df["Date"][0]
    data = np.array(data)
    data1= data[len(data)-10:]
    input_data =data1
    data_scaled = data1.reshape((n_past,1))

    data_scaled = scaler.transform(data_scaled).tolist()
    out_data = []
    i=0
    ran = len(data)-5
    while(i<ran):
        x_input=data_scaled[len(data_scaled)-n_past:]

        x_input=np.array(x_input).reshape((1,n_past,1))
        y_pred = model.predict(x_input)[0][0]
 
        actual_p =scaler.inverse_transform([[y_pred]]).tolist()
        out_data.append(actual_p[0][0])
        data_scaled.append([y_pred])
        i=i+1
    plt.figure(figsize=(20,10))
    datelist = pd.date_range(init_date , periods=len(data)+i-1)
    ax=sns.lineplot(datelist[:len(data)],data, label='Actual_Values', marker='o')
    ax=sns.lineplot(datelist[10:len(data)+5],out_data ,label='Predicted_Values', marker='o')
    ax.set_ylabel('DOGE Price in USD')
    ax.set_xlabel('Dates')
    plt.title(f"DOGE Price Prediction for Data of Days :{len(data)-5}")
    return (ax,out_data,datelist[10:len(data)+5])

def get_pred_shib():
    """
    for getting prediction on future 10 days from today on SHIB
    args:
            NO Argument Required
    returns :
            {matplolib.plot}: contains graph of actual data and model predicted values  
    
    """
    model = shib_model
    scaler = load(open('ReqFiles/scaler_shib.pkl', 'rb'))
    df=fetch_data(20,tickers='SHIB-USD')
    data =df['Close']
    init_date = df["Date"][0]
    data = np.array(data)
    data1= data[len(data)-10:]
   
    data_scaled = data1.reshape((n_past,1))

    data_scaled = scaler.transform(data_scaled).tolist()
    out_data = []
    i=0
    ran = len(data)-5
    while(i<ran):
        x_input=data_scaled[len(data_scaled)-n_past:]

        x_input=np.array(x_input).reshape((1,n_past,1))
        y_pred = model.predict(x_input)[0][0]
 
        actual_p =scaler.inverse_transform([[y_pred]]).tolist()
        out_data.append(actual_p[0][0])
        data_scaled.append([y_pred])
        i=i+1
    plt.figure(figsize=(20,10))
    datelist = pd.date_range(init_date , periods=len(data)+i-1)
    ax=sns.lineplot(datelist[:len(data)],data, label='Actual_Values', marker='o')
    ax=sns.lineplot(datelist[10:len(data)+5],out_data ,label='Predicted_Values', marker='o')
    ax.set_ylabel('SHIB Price in USD')
    ax.set_xlabel('Dates')
    plt.title(f"SHIB Price Prediction for Data of Days :{len(data)-5}")
    return (ax,out_data,datelist[10:len(data)+5])

