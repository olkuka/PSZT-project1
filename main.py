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


start = time.time()
NUM_ITER = 100
# INPUT_FILE = "cities.txt"

# with open(INPUT_FILE) as f:
#     cities = f.readlines()

# cities = [x.strip() for x in cities] 

# filter the table to include only the cities from the input file
# driving_distances = driving_distances[(driving_distances["Distance (km)"] \
# 	.isin(cities))][cities+["Distance (km)"]] \
# 	.set_index("Distance (km)")

population = Population(population_size=15)
iterations = []
path_lengths = []

for i in range(NUM_ITER):
	population = travellingSalesman.evolve(population)
	if not i%5:
		# print("Iteration number {}, best path is {}".format(i, population.find_fittest().path_km_length()))
		iterations.append(i)
		path_lengths.append(population.find_fittest().path_km_length())

	if not i%20:
		print("Iteration number {}, best path is {}".format(i, population.find_fittest().path_km_length()))

best_individual = population.find_fittest()
print("The best path is {}, length {}".format(best_individual.get_path(), best_individual.path_km_length()))

end = time.time()
print("TIME")
print(end - start)

sns.lineplot(x=iterations, y=path_lengths)
plt.show()
