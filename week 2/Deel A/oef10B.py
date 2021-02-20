import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("titanic.csv")

# welke Kolommen?
# print(df)

# Hoeveel personen?
tot = df["PassengerId"].count()
print("Er waren: ", tot, "personen")

# Hoeveel mannen
aantal_man = df[df["Sex"] == "male"].PassengerId.count()
print("Er waren: ", aantal_man, "mannen en: ", tot - aantal_man, "vrouwen")

# Hoeveel overleefd
overleefd_man = df[df["Survived"] == 1].where(df["Sex"] == "male").PassengerId.count()
overleefd_vrouw = df[df["Survived"] == 1].where(df["Sex"] != "male").PassengerId.count()
print("Er hebben: ", overleefd_man, "mannen het overleefd")
print("Er hebben: ", overleefd_vrouw, "vrouwen het overleefd")
print("Dit zijn er in totaal: ", overleefd_man + overleefd_vrouw)

# plt.hist(df["Age"])
# plt.grid(True)
# plt.show()

sns.countplot(x="Pclass", hue="Sex", data=df)
plt.show()
