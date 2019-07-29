import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statistics

a = [24.0, 25.0, 24.3, 25.5]
b = [25.3, 26.5, 26.4, 27.0, 27.6, 28.1, 19.4, 20.5]
c = [26.3, 24.0, 24.7, 21.2, 23.5]

print ("Mean 1: ", statistics.mean(a))
print ("Mean 2: ", statistics.mean(b))
print ("Mean 3: ", statistics.mean(c))
print ("Sigma 1: ", statistics.stdev(a))
print ("Sigma 2: ", statistics.stdev(b))
print ("Sigma 3: ", statistics.stdev(c))


fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=True)

# We can set the number of bins with the `bins` kwarg

n_bins = 100

axs[0].hist(a, bins=n_bins)
axs[1].hist(b, bins=n_bins)
axs[2].hist(c, bins=n_bins)

plt.show()