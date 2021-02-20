import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

df = pd.read_csv("heupbreedtes.csv")
_, bins, _ = plt.hist(df, 20, density=1, alpha=0.5)
mu, sig = norm.fit(df)
best_fit = norm.pdf(bins, mu, sig)
plt.plot(bins, best_fit)
plt.show()


def calcZScore(omtrek):
    return (int(omtrek) - mu) / sig


heup = input("Geef een heupbreedte in: ")
zscore = calcZScore(heup)
print("De Z-score hiervan is: ", zscore)
print(round((norm.cdf(zscore) * 100), 1), "% van de mannen heeft een kleinere breedte")
