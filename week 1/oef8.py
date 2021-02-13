import matplotlib.pyplot as plt


def func(x_val):
    return 2 * x_val + 3


x = list(range(0, 10))
y = []
for i in x:
    y.append(func(i))

plt.plot(x, y, "bo-")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend("y = 2x+3")
plt.show()

