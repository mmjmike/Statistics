import numpy as np
import random
import matplotlib.pyplot as plt

total_numbers = 20
sample_size = 3

population = range(1,1+total_numbers)

def generate_samples(population, sample_size):
    if sample_size == 0:
        new_set = [Sample()]
        return new_set
    current_set = generate_samples(population, sample_size - 1)
    new_set = []
    for sample in current_set:
        for element in population:
            new_sample = Sample(sample.elements.copy())
            if len(sample) > 0 and element <= sample.elements[-1]:
                continue
            else:
                new_sample.add_element(element)
                new_set.append(new_sample)
    return new_set


def plot_means(means):
    set_of_means = list(set(means))
    set_of_means.sort()
    bins = set_of_means
    frequencies = [means.count(mean)/len(means) for mean in set_of_means]
    plt.hist(means, bins, histtype='bar',label='distribution', color='c', rwidth=0.8)
    plt.xlabel('Sample means')
    plt.ylabel('Frequency')
    plt.title("Sample distribution")
    plt.show()


class Sample:

    def __init__(self, elements=list()):
        self.elements = elements

    @property
    def mean(self):
        return np.mean(self.elements)

    @property
    def min(self):
        return min(self.elements)

    @property
    def max(self):
        return max(self.elements)

    def add_element(self, new_element):
        self.elements.append(new_element)

    def __len__(self):
        return len(self.elements)

    def __str__(self):
        return ",".join(self.elements)


list_of_samples = generate_samples(population, sample_size)
list_of_means = [sample.mean for sample in list_of_samples]
plot_means(list_of_means)
