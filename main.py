#!/usr/bin/env python

"""main.py: ..."""

__author__ = "Aleksandra Kukawka, Bartłomiej Binda"
__copyright__ = "Copyright 2021, Podstawy Sztucznej Inteligencji"

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from download_data import driving_distances
# import helpers
from travellingSalesman import travellingSalesman
from individual import Individual
from population import Population

import time



NUM_ITER = 2000

# mutation_probabilities = [0.05, 0.1, 0.2, 0.3, 0.4]

population_sizes = [5, 15, 25, 50, 100]

start = time.time()
population = Population(population_size=15)
iterations = []
path_lengths = []

for i in range(NUM_ITER):
	population = travellingSalesman.evolve(population)
	if not i%5:
		print("Iteration number {}, best path is {}".format(i, population.find_fittest().path_km_length()))
		iterations.append(i)
		path_lengths.append(population.find_fittest().path_km_length())

	# if not i%500:
	# 	print("Iteration number {}, best path is {}".format(i, population.find_fittest().path_km_length()))

best_individual = population.find_fittest()
print("The best path is {}, length {}".format(best_individual.get_path(), best_individual.path_km_length()))

end = time.time()
print("TIME")
print(end - start)
print()

sns.lineplot(x=iterations, y=path_lengths)
plt.show()
