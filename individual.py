#!/usr/bin/env python

"""individual.py: individual class implementation
Includes all methods for a single individual"""

__author__ = "Aleksandra Kukawka, Bartłomiej Binda"
__copyright__ = "Copyright 2021, Podstawy Sztucznej Inteligencji"

from download_data import driving_distances
import random


CITIES = driving_distances.index.tolist()


class Individual():
    def __init__(self, distances_table=driving_distances, path=None):
        """Makes a new individual. If we don't provide a path 
        then we create an individual with random path"""
        self.cities = CITIES
        self.distances_table = distances_table
        if path==None:
            self.path = self.create_random_individual(self.cities)
        else:
            self.path = path[:]

    def create_random_individual(self, nodes):
        """Randomly shuffles list to create a random path"""
        return [nodes[0]] + random.sample(nodes[1:], len(nodes)-1)

    def get_path(self):
        return self.path

    def set_path(self, new_path):
        self.path = new_path

    def append_path(self, gene):
        """"Adds gene to existing path"""
        self.path.append(gene)

    def get_gene(self, index):
        return self.path[index]

    def set_gene(self, index, new_gene):
        self.path[index] = new_gene

    def get_length(self):
        return len(self.path)

    def get_fitness(self):
        """Calculates fitness of the path"""
        return 1 / self.path_km_length()
    
    def path_km_length(self):
        """Given some path of cities evaluates how long the path is in km
        Returns integer"""
        path_length = 0
        origin = self.path[0]

        for destination in self.path[1:]+[self.path[0]]:
            path_length += int(self.distances_table[self.distances_table.index == origin][destination])
            origin = destination

        return path_length

        