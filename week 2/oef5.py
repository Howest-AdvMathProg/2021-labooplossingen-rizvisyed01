import pandas as pd

df = pd.read_csv("euro2012.csv")

filter = df[df["Team"].str.startswith('G')]
res = filter[["Team", "Goals"]]
print(res)
