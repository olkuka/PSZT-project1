#!/usr/bin/env python

"""main.py: ..."""

__author__ = "Aleksandra Kukawka, Bartłomiej Binda"
__copyright__ = "Copyright 2021, Podstawy Sztucznej Inteligencji"

from individual import Individual


class Population():
    def __init__(self, population_size=0, initialise=True):
        self.individuals = []
        if initialise:
            self.individuals = [Individual() for _ in range(population_size)]

    def get_individual(self, index):
        return self.individuals[index]

    def get_individuals(self):
        return self.individuals

    def find_fittest(self):
        individuals_fitness = [ind.get_fitness() for ind in self.individuals]
        max_fitness = max(individuals_fitness)
        max_index = individuals_fitness.index(max_fitness)
        return self.individuals[max_index]

    def find_worst(self):
        individuals_fitness = [ind.get_fitness() for ind in self.individuals]
        min_fitness = min(individuals_fitness)
        min_index = individuals_fitness.index(min_fitness)
        return self.individuals[min_index]

    def append_individual(self, individual):
        self.individuals.append(individual)

    def remove_individual(self, individual):
        self.individuals.remove(individual)

    def get_size(self):
        return len(self.individuals)

