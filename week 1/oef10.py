import matplotlib.pyplot as plt
import math


# 1.Teken de grafiek van deze functie
def bal_fun(t_val):
    return 95 - 9 * t_val - 2 * (t_val ** 2)


x = []
y = []

for i in range(-10, 10):
    x.append(i)
    y.append(bal_fun(i))

plt.plot(x, y, "r-")
plt.xlabel("Time")
plt.ylabel("Height")

plt.ylim(0, max(y) + 10)
plt.show()


# 2.Hoelang duurt de vlucht?
# afstand tussen de nullpunten is de duur van de vlucht

def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)


def zeros(a, b, D):
    return [(-b - math.sqrt(D)) / (2 * a),
            (-b + math.sqrt(D)) / (2 * a)]


def dist_points(p1, p2):
    return abs(p1 - p2)


zeros_graph = zeros(-2, -9, discriminant(-2, -9, 95))
print(zeros_graph)
print("2: Hij vliegt voor ", dist_points(zeros_graph[0], zeros_graph[1]), "uren")

# 3.Op het ogenblik dat we boven het zwembad vliegen, hoe lang zijn we dan al in de lucht?
# Tijd start vanaf dit punt, we zoeken dus de afstand van het eerste nullpunt en T = 0

print("3: We zijn al  ", dist_points(-9.5, 0), "uren in de lucht")

# 4.Hoe hoog ben je op het ogenblik dat je boven het zwembad vliegt?
print("4: Boven het zwembad is t = 0 dus: ", bal_fun(0), "meter")

# 5.Hoelang vlieg je hoger dan 39 meter?
# we doen een analoge berekening voor om de nullpunten te vinden maar inplaats
# van het snijpunt met de X as te vinden (x=0) zoeken we deze met de rechte X = 39
# 39 = 95 -9t -2t^2 <=> 0 = 56 - 9t -2t^2

intersect_39 = zeros(-2, -9, discriminant(-2, -9, 56))
print("5: Hij is voor ", dist_points(intersect_39[0], intersect_39[1]), "uren boven de 39 m")

# 6.Als t = 0 het vertrek zou moeten zijn, hoe ziet het nieuwe functievoorschrifter dan uit?
# Wat gebeurt er met de grafiek van de functie?

# Dit zal zorgen dat de grafiek opschuift naar rechts
# het linkse nulpunt moet 0 worden dus +9.5, dit analoog bij de rechtse wat dus 14.5 wordt
# de afstand hiertussen is dus nog steeds 14.5 wat klopt met oef 2
# we weten de nullpunten, ook hebben we een extra punt nodig. Deze halen we uit het gegeven
# dat op t = 0 deze 95 meter hoog is, op onze nieuw grafiek zal dit t= 9.5 zijn met hoogte 95
# deze komt terug overeen met resultaten van oef 3
# we gebruiken deze gegevens in volgende formule namelijk: h(t) = a(t-t1)(t-t2)
# t1 en t2 zijn de nulpunten en met behulp van ons punt (9.5, 95) kunnen we a vinden
# namelijk -2
# het voorschrift is dus h(t) = -2(x-0)(x-14.5)
# OF
#  h(t) = -2x^2 + 29x

