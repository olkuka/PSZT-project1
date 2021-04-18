#!/usr/bin/env python

"""population.py: population class implementation
Includes all methods for the whole population of individuals"""

__author__ = "Aleksandra Kukawka, Bartłomiej Binda"
__copyright__ = "Copyright 2021, Podstawy Sztucznej Inteligencji"

from individual import Individual

import numpy as np


class Population():
    def __init__(self, population_size=0, initialise=True):
        """Given population size creates new population with empty
        Individuals"""
        self.individuals = []
        if initialise:
            self.individuals = [Individual() for _ in range(population_size)]

    def get_individual(self, index):
        return self.individuals[index]

    def find_fittest(self):
        """Finds and returns the fittest individual of the whole population"""
        individuals_fitness = [ind.get_fitness() for ind in self.individuals]
        max_fitness = max(individuals_fitness)
        max_index = individuals_fitness.index(max_fitness)
        return self.individuals[max_index]

    def find_many_fittest(self, size):
        """Given size finds and returns as much fittest individuals
        as size demands"""
        individuals_fitness = np.array([ind.get_fitness() for ind in self.individuals])
        if size == 0:
            max_indices = []
        else:
            max_indices = np.argpartition(individuals_fitness, -size)[-size:]
        return [self.individuals[index] for index in max_indices]

    def find_worst(self):
        """Finds and returns the worst individual of the whole population"""
        individuals_fitness = [ind.get_fitness() for ind in self.individuals]
        min_fitness = min(individuals_fitness)
        min_index = individuals_fitness.index(min_fitness)
        return self.individuals[min_index]

    def append_individual(self, individual):
        """Appends individual to the population"""
        self.individuals.append(individual)

    def remove_individual(self, individual):
        """Removes individual to the population"""
        self.individuals.remove(individual)

    def get_size(self):
        return len(self.individuals)

