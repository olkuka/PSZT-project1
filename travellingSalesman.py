#!/usr/bin/env python

"""main.py: ..."""

__author__ = "Aleksandra Kukawka, Bartłomiej Binda"
__copyright__ = "Copyright 2021, Podstawy Sztucznej Inteligencji"

from individual import Individual
from population import Population
import random


class travellingSalesman():
    # Constants
    crossover_probability = 0.5
    mutation_probability = 0.2
    tournament_size = 2
    elitism = True
    permutation_number = 5


    @staticmethod
    def evolve(population):
        evolved_population = Population(population.get_size(), initialise=False)
        start = 0

        if travellingSalesman.elitism:
            evolved_population.append_individual(population.find_fittest())
            # evolved_population.worst_individual = population.get_individual(0)
            # start = 1
        
        for i in range(start, population.get_size()):
            individual1 = travellingSalesman.tournament_selection(population)
            individual2 = travellingSalesman.tournament_selection(population)

            new_individual = travellingSalesman.crossover(individual1, individual2)
            evolved_population.append_individual(new_individual)

            # checking if new_individual is not the worst individual to remove in a succession step 
            # (only if elitism is True)
            if travellingSalesman.elitism:
                # if we're in the beginning and don't have worst_individual yet 
                if i == start:
                    evolved_population.worst_individual = new_individual
                # otherwise
                elif new_individual.get_fitness() < evolved_population.worst_individual.get_fitness():
                    evolved_population.worst_individual = new_individual

        for i in range(start, population.get_size()):
            if random.random() <= 0.5:
                travellingSalesman.inverse_mutation(evolved_population.get_individual(i))
            else:
                travellingSalesman.inverse_mutation(evolved_population.get_individual(i))

        evolved_population.remove_worst_individual

        return evolved_population

    @staticmethod
    def crossover(individual1, individual2):
        if random.random() <= travellingSalesman.crossover_probability:
            first_parent = individual1
            second_parent = individual2
        else:
            first_parent = individual2
            second_parent = individual1

        child = Individual()
        
        first_cut, second_cut = sorted(random.sample(range(0, first_parent.get_length()), 2))
        child.set_path(first_parent.get_path()[first_cut:second_cut+1])

        for gene in second_parent.get_path():
            if gene not in child.get_path():
                child.append_path(gene)

        return child

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
        samples = [population.get_individuals()[index] for index in indices]
        # ind.fitness available with class, for one sort scores?
        selected = sorted(samples, key=lambda ind: ind.get_fitness(), reverse=True)[0]
        
        return selected