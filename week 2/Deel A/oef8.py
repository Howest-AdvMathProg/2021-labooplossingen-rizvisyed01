import pandas as pd

df = pd.read_csv("euro2012.csv")

print(df.iloc[:, 0:-6])
