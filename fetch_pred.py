'''
This is python to serve data with prediction graph and datetime data to the Flask App

'''

import tensorflow as tf  # for model loading 
import matplotlib.pyplot as plt  # plotting purpoes
import numpy as np   # mathamatical purpoes
import pandas as pd   # data manupilation
import seaborn as sns  # plotting graph
from fetch_data import fetch_data   # self-defined library to fetch data dynamically
from pickle import load    # loading .pkl files 


'''
Loading trained model , model training files are in Model Building Files directory
'''
btc_model =tf.keras.models.load_model('ReqFiles/LSTM_V2_BTC.h5')
eth_model = tf.keras.models.load_model('ReqFiles/LSTM_V2_ETH.h5')
doge_model= tf.keras.models.load_model('ReqFiles/LSTM_V2_DOGE.h5')
shib_model= tf.keras.models.load_model('ReqFiles/LSTM_V2_SHIB.h5')


#   model is trained as 10 days of input so mentioning it in n_past
n_past = 10


#  Function for bitcoin to deliver prediction values upto 10 days
def get_pred_btc():
    """
    for getting prediction on future 10 days from today on bitcoin
    args:
            NO Argument Required
    returns :
            {matplolib.plot}: contains graph of actual data and model predicted values  
    
    """
    model = btc_model
#      Loading minmaxscaler that is used while training model
    scaler = load(open('ReqFiles/scaler_btc.pkl', 'rb'))
#     Fetching  data from yfinace using fun for 20 days of data of bitcoin in usd
    df=fetch_data(20 ,tickers='BTC-USD')
    data =df['Close']
    init_date = df["Date"][0]
#      converting data to array for model prediction
    data = np.array(data)
#      here taking 10 values as input and 1 day value as a output so considering first 10 days values for evaluation
    data1= data[:10]
#      reshaping data accoring to model purpoes
    data_scaled = data1.reshape((n_past,1))
#   transforming values using minmaxscaler same as used for training
    data_scaled = scaler.transform(data_scaled).tolist()
    out_data = []
    i=0
#     decalring ran variable to predict values upto 5 days
    ran = len(data)-5
#     using while loop , made a pipeline that will take 10 days of value and make prediction of 1 day and append 
#                                                            this prediction in data of 10 days that will used as input for next prediction 
    while(i<ran):
        x_input=data_scaled[len(data_scaled)-n_past:]   # taking last 10 days of data for input

        x_input=np.array(x_input).reshape((1,n_past,1))  # reshaping input in 3d form as per model requirement 
        y_pred = model.predict(x_input)[0][0]   #  model returns output in 2d array so taking only value in considaration
#         applying inverse transform to convert scaled values to user understandable form
        actual_p =scaler.inverse_transform([[y_pred]]).tolist()
        out_data.append(actual_p[0][0])
        data_scaled.append([y_pred])
        i=i+1
#   setting up figure size
    plt.figure(figsize=(20,10))
#      getting date series to visualise data in better way
    datelist = pd.date_range(init_date , periods=len(data)+i-1)
#  plot for actual values
    ax=sns.lineplot(datelist[:len(data)],data, label='Actual_Values', marker='o')
#     plot for predicted values
    ax=sns.lineplot(datelist[10:len(data)+5],out_data ,label='Predicted_Values', marker='o')
#      setting up label for both axis
    ax.set_ylabel('Bitcoin Price in USD')
    ax.set_xlabel('Dates')
#     placing title for plot
    plt.title(f"Bitcoin Price Prediction for Data of Days :{len(data)-10}")
#     returning ax as graph plot And out_data,datelist for displying prediction table
    return (ax,out_data,datelist[10:len(data)+5])



# Working same as get_pred_btc()  with change as Etherem coin
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
    plt.title(f"Etherum Price Prediction for Data of Days :{len(data)-10}")
    return (ax,out_data,datelist[10:len(data)+5])
# Working same as get_pred_btc()  with change as Doge coin
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
    plt.title(f"DOGE Price Prediction for Data of Days :{len(data)-10}")
    return (ax,out_data,datelist[10:len(data)+5])
# Working same as get_pred_btc()  with change as SHIB coin
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
    plt.title(f"SHIB Price Prediction for Data of Days :{len(data)-10}")
    return (ax,out_data,datelist[10:len(data)+5])

