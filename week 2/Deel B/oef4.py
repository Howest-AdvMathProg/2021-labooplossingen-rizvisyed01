import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("student-mat.csv", header=0, delimiter=";")
print(df.head())

# Hoeveel studenten steken in de dataset?
print("Er zitten ", df.sex.count(), "studenten")
# Gebruik de describe-functie om een overzicht te bekomen van de variabelen in de dataset
print(df.describe())
# Bepaal het geslacht en de leeftijd van de vijf studenten met de beste score
highest_five = df.nlargest(5, "G3")
print(highest_five[["sex", "age", "G3"]])
# Gebruik een countplot om een staafdiagramma met de leeftijden weer te geven

# sns.countplot(x="age", data=df)

# We focussen ons nu op de leeftijd van de studenten.
ages = df['age']
# Bereken de volgende centrummaten en de spreidingsmaten
# -Het gemiddelde
print("Gemiddelde: ", ages.mean())
# -De mediaan
print("Median: ", ages.median())
# -Variantie
print("Variance: ", ages.var())
# -Standaardafwijking
print("Standard: ", ages.std())
# -De range
print("Range: ", ages.max() - ages.min())
# -Q1 en Q3 en bereken hieruit de interkwartielafstand
print("IQR: ", ages.quantile(0.75) - ages.quantile(0.25))
# -scheefheid
print("Skew: ", ages.skew())
# -De kurtosis
print("Skew: ", ages.kurt())
# Bepaal een boxplot van de leeftijd(voorbeeld zie onder)

# sns.boxplot(x=df["age"])

# Kan je ook een onderscheid maken tussen mannen en vrouwen?
sns.boxplot(x=df["sex"], y=df["age"])

plt.show()
