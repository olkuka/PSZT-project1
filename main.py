#!/usr/bin/env python

"""main.py: ..."""

__author__ = "Aleksandra Kukawka, Bartłomiej Binda"
__copyright__ = "Copyright 2021, Podstawy Sztucznej Inteligencji"

import pandas as pd

from download_data import driving_distances
import helpers


INPUT_FILE = "cities.txt"

with open(INPUT_FILE) as f:
    cities = f.readlines()

cities = [x.strip() for x in cities] 

# filter the table to include only the cities from the input file
driving_distances = driving_distances[(driving_distances["Distance (km)"] \
	.isin(cities))][cities+["Distance (km)"]] \
	.set_index("Distance (km)")

for i in range(3):
	individual = helpers.create_individual(cities)

	print(individual)

	print(helpers.evaluate_path(individual, driving_distances))
