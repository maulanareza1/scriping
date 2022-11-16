import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_quote.csv')
plt.rcParams["figure.aoutolayout"] = True
fig, ax = plt.subplots()
df['author'].value_counts().plot(ax = ax, kind="barh")
plt.show()

# print(df['author'].value_counts().to_string())