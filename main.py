#!/usr/bin/env python

"""main.py: Main file"""

__author__ = "Aleksandra Kukawka, Bartłomiej Binda"
__copyright__ = "Copyright 2021, Podstawy Sztucznej Inteligencji"

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from download_data import driving_distances
from travellingSalesman import travellingSalesman
from individual import Individual
from population import Population

import time


NUM_ITER = 2000

# start measuring time
start = time.time()

# set population size
population = Population(population_size=15)

# store number of iterations and path lengths to create plot in the end
iterations = []
path_lengths = []

# main for loop
for i in range(NUM_ITER):
	population = travellingSalesman.evolve(population)

	if not i%5:
		iterations.append(i)
		path_lengths.append(population.find_fittest().path_km_length())

	# prints best path every 500
	if not i%500:
		print("Iteration number {}, best path is {}".format(i, population.find_fittest().path_km_length()))

best_individual = population.find_fittest()
print("The best path is {}, length {}".format(best_individual.get_path(), best_individual.path_km_length()))

# end measuring time
end = time.time()

print("TIME")
print(end - start)
print()

# visualize the results
sns.lineplot(x=iterations, y=path_lengths)
plt.show()

