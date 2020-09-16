import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stock_csv_path_googleJ = r"C:\Users\starriet\Downloads\GOOG.csv"

df = pd.read_csv(stock_csv_path_googleJ)
print(type(df.index))
print(type(df.index[0]))
print(df.head())

df = pd.read_csv(stock_csv_path_googleJ, index_col='Date')
print(df.index)
print(type(df.index))
print(type(df.index[0]))
print(df.head())

df = pd.read_csv(stock_csv_path_googleJ, index_col='Date', parse_dates=['Date'])
print(df.index)
print(type(df.index))
print(type(df.index[0]))
print(df.head())

print('---------------------------')
print(df.loc[:,['Adj Close']])
df.loc[:,['Adj Close']].plot(figsize=(16,9))
# adjClose = df.loc[:,['Adj Close']].copy()
# adjClose.plot(figsize=(16,9))

plt.show()

print(df.loc[:,['Adj Close']].plot(figsize=(16,9)))