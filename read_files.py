import pandas as pd

def read_Nin():
    df = pd.read_csv('Nintendo_2016-20.csv')
    df['Date'] = pd.to_datetime(df['Date'])

    return (df['Date'][::-1]), (df['Close'][::-1])