import numpy as np
import matplotlib.pyplot as plt
from math import e


def ex(x, minus):
    if minus:
        return -1 * e ** -x
    else:
        return e ** x


fig = plt.figure()

x_values = np.arange(0, 2.25, 0.25)
y_values_1 = []
y_values_2 = []

for x in x_values:
    y_values_1.append(ex(x, True))
    y_values_2.append(ex(x, False))

plt.plot(x_values, y_values_1, 'r-', x_values, y_values_2, "b--")
plt.show()
