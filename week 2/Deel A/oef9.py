import pandas as pd

df = pd.read_csv("euro2012.csv")

print(df[df["Team"].isin(["Russia", "England", "Italy"])].loc[:, ["Team", "Shooting Accuracy"]])
