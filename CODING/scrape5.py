import pandas as pd

df = pd.read_csv('data_quote.csv')
# print(df.columns)
# print(df.head())
# print(df.tail())
# print(df['author'].to_string())
print(df['author'].value_counts().to_string())