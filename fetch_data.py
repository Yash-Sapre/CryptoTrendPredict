import numpy as np
import pandas as pd
import yfinance as yf

def fetch_data (upto_dates = 10 , tickers='BTC-USD'):
  data = yf.download(tickers=tickers, period = f'{upto_dates}d', interval = '1d')
  new_array = np.array(data.index.to_pydatetime(), dtype=np.datetime64)
  o = data.iloc[: , 0].values
  h = data.iloc[: , 1].values
  l = data.iloc[: , 2].values
  c = data.iloc[: , 3].values
  df= pd.DataFrame(new_array)
  df.columns = ['Date']
  df['Open']=o
  df['High']=h
  df['Low']=l
  df['Close']=c
  return df

if __name__=='__main__':
    a=fetch_data()

    print(a)