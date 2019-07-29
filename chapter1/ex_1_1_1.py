import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statistics

a = [120, 150, 210, 250, 260, 270, 510, 870, 980, 1140]
b = [110, 160, 350, 400, 410, 430, 500, 520, 530, 570]

print ("Mean 1: ", statistics.mean(a))
print ("Mean 2: ", statistics.mean(b))
print ("Sigma 1: ", statistics.stdev(a))
print ("Sigma 2: ", statistics.stdev(b))


fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the `bins` kwarg

n_bins = 100

axs[0].hist(a, bins=n_bins)
axs[1].hist(b, bins=n_bins)



plt.show()

