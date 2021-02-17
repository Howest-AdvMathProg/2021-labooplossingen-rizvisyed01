
import pandas as pd

df = pd.read_csv("euro2012.csv")

print("The mean yellow is: ", df["Yellow Cards"].mean())
