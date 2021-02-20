from scipy.stats import norm

gem = 100
std = 15

print("Het percentage is: ", round((norm.sf(130, loc = 100, scale = 15))*100, 2))
