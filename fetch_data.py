'''
          Works as interface to provide crypto values data
'''
import numpy as np   # mathamatical purpoes
import pandas as pd   # data manupilation
import yfinance as yf  # it is api that will fetch crypto values as per need 


#  function that will used by other python files 
def fetch_data (upto_dates = 10 , tickers='BTC-USD'):
  '''
  Arguments :
              upto_dates : it eill fetch values upto days , by default 10 days , it should be an integer
              tickers  : fetching metioned crypot data with currency , by default BTC with USD , use format  "'crypto_name'-'currancy'"
  Returns   :
            dataframe consisting of tickers corresponding values of High , Low , Open , Close and Date
  
  '''
  data = yf.download(tickers=tickers, period = f'{upto_dates}d', interval = '1d') # download data of tickers for upto_dates with 1 day as interval 
#   data variable containes pd.Dataframe of crypto values with index as dates
  new_array = np.array(data.index.to_pydatetime(), dtype=np.datetime64)  # converting dates from index of data to array
  #  getting "Open" Values from data
  o = data.iloc[: , 0].values
   #  getting "High" Values from data
  h = data.iloc[: , 1].values
   #  getting "Low" Values from data
  l = data.iloc[: , 2].values
   #  getting "Close" Values from data
  c = data.iloc[: , 3].values
  #  Creating Dataframe consisting  Date as columns 
  df= pd.DataFrame(new_array)
  df.columns = ['Date']  # naming column as Date
  df['Open']=o  # creating new column Open and storing values from 'Open' of Data
  df['High']=h # creating new column High and storing values from 'High' of Data
  df['Low']=l # creating new column Low and storing values from 'Low' of Data
  df['Close']=c # creating new column Close and storing values from 'Close' of Data
  return df   # returing dataframe

if __name__=='__main__':  # only for file testing purpoes 
    a=fetch_data() 
    print(a)