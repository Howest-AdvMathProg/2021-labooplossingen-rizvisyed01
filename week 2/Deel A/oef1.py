import numpy as np
import pandas as pd

df = pd.read_csv("euro2012.csv")

goals = df["Goals"]
teams = df["Team"]
print("Goals")
print("---------------")
print(goals)

print("Teams")
print("---------------")
print(teams)
