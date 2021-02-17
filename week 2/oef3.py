import pandas as pd

df = pd.read_csv("euro2012.csv")
teams_cards = df[["Team", "Red Cards", "Yellow Cards"]]
print(teams_cards)
teams_cards.sort_values(by=["Red Cards", "Yellow Cards"])

