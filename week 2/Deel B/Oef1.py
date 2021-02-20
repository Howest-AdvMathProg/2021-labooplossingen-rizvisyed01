import matplotlib.pyplot as plt
import numpy as np
import math

values = [[0, 1], [-1, 1], [0, 2], [2, 3]]


def guass(x, µ, sigma):
    return (1 / (np.sqrt(2 * math.pi) * sigma)) * (np.exp(-1 * ((x - µ) ** 2 / (2 * (sigma ** 2)))))


x_values = np.linspace(0 - 3 * 1, 0 + 3 * 1, 100)

for value in values:
    plt.plot(x_values, guass(x_values, value[0], value[1]))

plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
