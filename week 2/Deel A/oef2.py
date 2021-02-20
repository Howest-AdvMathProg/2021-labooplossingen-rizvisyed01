import numpy as np
import pandas as pd

df = pd.read_csv("euro2012.csv")

print("Er zijn zoveel teams: ", df['Team'].count())