#!/usr/bin/env python

"""main.py: ..."""

__author__ = "Aleksandra Kukawka, Bartłomiej Binda"
__copyright__ = "Copyright 2021, Podstawy Sztucznej Inteligencji"

import pandas as pd

from download_data import driving_distances
# import helpers
from travellingSalesman import travellingSalesman
from individual import Individual
from population import Population


NUM_ITER = 1000
# INPUT_FILE = "cities.txt"

# with open(INPUT_FILE) as f:
#     cities = f.readlines()

# cities = [x.strip() for x in cities] 

# filter the table to include only the cities from the input file
# driving_distances = driving_distances[(driving_distances["Distance (km)"] \
# 	.isin(cities))][cities+["Distance (km)"]] \
# 	.set_index("Distance (km)")

# for i in range(3):
# 	individual = helpers.create_individual(cities)

# 	print(individual)

# 	print(helpers.evaluate_path(individual, driving_distances))

population = Population(population_size=15)

for i in range(NUM_ITER):
	population = travellingSalesman.evolve(population)
	if not i%20:
		print("Iteration number {}, best path is {}".format(i, population.find_fittest().path_km_length()))

best_individual = population.find_fittest()
print("The best path is {}, length {}".format(best_individual.get_path(), best_individual.path_km_length()))

