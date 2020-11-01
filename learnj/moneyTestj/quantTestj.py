import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

google_csv = r'C:\Users\starriet\Downloads\GOOG.csv'

# df = pd.read_csv(google_csv, )
# df = pd.read_csv(google_csv, index_col='Date',)
df = pd.read_csv(google_csv, index_col='Date', parse_dates=['Date'])
print(len(df))
# print(df.head())
# print(df.index)
# print(type(df.index[0]))

# # i. 결측치 있나 체크. ->없음.
# print(df[df.isin([np.nan, -np.inf, np.inf]).any(1)])

df_price = df.loc[:, ['Adj Close']].copy()
# df_price.plot(figsize=(10,6))
# plt.show()

# from_date = '2005-01-01'
# to_date = '2007-03-01'
# df_price.loc[from_date:to_date].plot(figsize=(16,9))
# plt.show()

df_price['day_rtn'] = df_price['Adj Close'].pct_change()
print(df_price.head())
# df_price['day_rtn']+=1
# print(df_price.head()) # i. 예상대로 모든값에 1 더해짐.
df_price['cum_rtn'] = (df_price['day_rtn']+1).cumprod()
print(df_price.head())
print(df_price.tail())
