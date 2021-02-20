import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("euro2012.csv")

filtered_data = df[np.logical_and(df.Goals > 4, df.Goals < 11)].loc[:,
                ["Team", "Goals", "Penalty goals", "Shots on target"]]

print(filtered_data.sort_values(by=(["Goals"]), ascending=False))

filtered_data.plot(x="Team", y=["Goals", "Shots on target"], kind='barh')
plt.grid(True)
plt.show()


