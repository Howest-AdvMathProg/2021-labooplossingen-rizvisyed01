# standaard normale verdeling is gemiddelde van 0 en std van 1
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

randoms = np.sort(np.random.randn(1000))
print(type(randoms))
print("Gemiddelde: ", np.mean(randoms))
print("Std: ", np.std(randoms))

# We stellen vast dat deze zeer dicht liggen bij de parameters van de
# standaard normaal verdeling

# als density true is zal et voorgesteld worden hoeveel
# percent van de gegevens in de respectievelijk bin zit
# fig, ax = plt.subplots(2)
# fig.suptitle("Difference histograms")
# ax[1].hist(randoms, density=True)
# ax[0].hist(randoms, density=False)

_, bins, _ = plt.hist(randoms, 20, density=1, alpha=0.5)
mu, sig = norm.fit(randoms)
best_fit = norm.pdf(bins, mu, sig)
plt.plot(bins, best_fit)
plt.show()
