import pandas as pd
import numpy as np

s1 = pd.Series([1, np.nan, 3, 4, 5])
s2 = pd.Series([1, 2, np.nan, 4, 5])
s3 = pd.Series([1, 2, 3, 4, 5])
# print(s1)

df = pd.DataFrame({'s1':s1, 's2':s2, 's3':s3})
# print(df.head())

print(df['s1'].isna())
print(df.isna())
print(df.isna().sum())

print('lllllllllllllllllllllllllllllllllllllllllllll')
print(df[df.isin([np.nan, np.inf, -np.inf]).any(1)])