#!/usr/bin/env python

"""download_data.py: this file is downloading data from engineeringtoolbox
Data: table of distances between 37 European cities
"""

__author__ = "Aleksandra Kukawka, Bartłomiej Binda"
__copyright__ = "Copyright 2021, Podstawy Sztucznej Inteligencji"

import pandas as pd


# read all the tables with the distances to all the cities
all_tables = pd.read_html(
    "https://www.engineeringtoolbox.com/driving-distances-d_1029.html?fbclid=IwAR3IRT_NBVFnCNvfeD4lyXZbHmpbYYNLBOnz3dNGrnoYFSJDungHX-2QUDk"
)

# merge all the tables into one big dataframe containing all city pairs
driving_distances = all_tables[0]
for table in all_tables[1:]:
    driving_distances = pd.merge(driving_distances, table)

driving_distances.set_index("Distance (km)", inplace=True)

