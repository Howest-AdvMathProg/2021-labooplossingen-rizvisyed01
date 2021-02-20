import pandas as pd

df = pd.read_csv("euro2012.csv")
teams_cards = df[["Team", "Red Cards", "Yellow Cards"]]
filterd_df = df.loc[:, ["Team", "Yellow Cards", "Red Cards"]]
filterd_df_sorted = filterd_df.sort_values(by=['Red Cards', "Yellow Cards"], ascending=False)

print(filterd_df_sorted)