import matplotlib.pyplot as plt

x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
circle = [3.14159, 12.56636, 28.27431, 50.26544, 78.53975, 113.09724]
square = [1.0, 4.0, 9.0, 16.0, 25.0, 36.0]

plt.plot(x, circle, "b-", x, square, "ro--")
plt.ylabel("Area")
plt.xlabel("Radius/Side")
plt.legend(["Circle", "Square"])
plt.show()
