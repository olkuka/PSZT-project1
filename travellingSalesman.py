#!/usr/bin/env python

"""
travellingSalesman.py: travellingSalesman class implementation
Includes all methods needed to perform the genetic algorithm
"""

__author__ = "Aleksandra Kukawka, Bartłomiej Binda"
__copyright__ = "Copyright 2021, Podstawy Sztucznej Inteligencji"

from individual import Individual
from population import Population
import random


class travellingSalesman():
    # Constants
    crossover_probability = 0.8
    mutation_probability = 0.1
    elitism = True
    permutation_number = 5
    tournament_size = 3


    @staticmethod
    def evolve(population, elitism_size=None):
        """
        main genetic algorithm function (one iteration)
        """
        if elitism_size == None:
            # set default elitism size to 1
            elitism_size = 1

        evolved_population = Population(initialise=False)
        start = 0

        if travellingSalesman.elitism:
            best_individuals = population.find_many_fittest(elitism_size)
            for individual in best_individuals:
                evolved_population.append_individual(individual)
            start += elitism_size
        
        for i in range((population.get_size() + 1) // 2):
            individual1 = travellingSalesman.tournament_selection(population)
            individual2 = travellingSalesman.tournament_selection(population)

            new_individual1, new_individual2 = travellingSalesman.crossover(individual1, individual2)
            evolved_population.append_individual(new_individual1)
            evolved_population.append_individual(new_individual2)

        for i in range(start, evolved_population.get_size()):
            current_individual = evolved_population.get_individual(i)
            if random.random() <= 0.5:
              travellingSalesman.inverse_mutation(current_individual)
            else:
              travellingSalesman.scramble_mutation(current_individual)

        """
        remove worst elements until the size matches the previous population
        this will remove k (elitism_size) worst individuals
        if the population size is odd this will remove k+1 individuals (because our crossover appends two children each step)
        """
        while evolved_population.get_size() != population.get_size():
            evolved_population.remove_individual(evolved_population.find_worst())

        return evolved_population

    @staticmethod
    def crossover(individual1, individual2):
        if random.random() <= travellingSalesman.crossover_probability:
            first_parent = individual1
            second_parent = individual2
        else:
            return Individual(path=individual1.get_path()), Individual(path=individual2.get_path())

        child1 = Individual()
        child2 = Individual()
        
        first_cut, second_cut = sorted(random.sample(range(0, first_parent.get_length()), 2))
        
        child1.set_path(first_parent.get_path()[first_cut:second_cut+1])

        for gene in second_parent.get_path():
            if gene not in child1.get_path():
                child1.append_path(gene)

        child2.set_path(second_parent.get_path()[first_cut:second_cut+1])

        for gene in first_parent.get_path():
            if gene not in child2.get_path():
                child2.append_path(gene)

        return child1, child2

    @staticmethod
    def inverse_mutation(individual):
        if random.random() <= travellingSalesman.mutation_probability:
            first_cut, second_cut = sorted(random.sample(range(0, individual.get_length()), 2))
            previous_path = individual.get_path()
            individual.set_path(previous_path[:first_cut] + previous_path[first_cut:second_cut+1][::-1] + previous_path[second_cut+1:])

    @staticmethod
    def scramble_mutation(individual):
        if random.random() <= travellingSalesman.mutation_probability:
            current_path = individual.get_path()
            permutation_samples = random.sample(current_path, travellingSalesman.permutation_number)
            indices = [current_path.index(sample) for sample in permutation_samples]
            random.shuffle(permutation_samples)
            for i in range(len(permutation_samples)):
                individual.set_gene(indices[i], permutation_samples[i])

    @staticmethod
    def tournament_selection(population):
        """
        Tournament selection to find individuals for crossover
        """
        indices = random.sample(range(population.get_size()), travellingSalesman.tournament_size)
        samples = [population.get_individual(index) for index in indices]
        # ind.fitness available with class, for one sort scores?
        selected = sorted(samples, key=lambda ind: ind.get_fitness(), reverse=True)[0]
        
        return selected