import pandas as pd

df = pd.read_csv("euro2012.csv")

choice = input("Hoeveel kolommen wilt U zien?: ")

print(df.iloc[:, 0:int(choice)])
