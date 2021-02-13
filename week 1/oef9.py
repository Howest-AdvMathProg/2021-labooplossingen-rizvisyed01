import matplotlib.pyplot as plt


def fun_plane(x_val):
    return -2 * x_val + 100


def fun_rock(x_val):
    return -(x_val ** 2) + 3 * x_val + 106


x = list(range(0, 10))
y_plane = []
y_rocket = []

for i in x:
    y_plane.append(fun_plane(i))
    y_rocket.append(fun_rock(i))

plt.plot(x, y_plane, "r-", x, y_rocket, "b-")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
