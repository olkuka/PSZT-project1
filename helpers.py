#!/usr/bin/env python

"""main.py: ..."""

__author__ = "Aleksandra Kukawka, Bartłomiej Binda"
__copyright__ = "Copyright 2021, Podstawy Sztucznej Inteligencji"

import random


def create_individual(nodes):
	"""Randomly shuffles list to create a random path"""
	return [nodes[0]] + random.sample(nodes[1:], len(nodes)-1)

def evaluate_path(path, distances_table):
	"""Given some path of cities evaluates how long the path is in km
	Returns integer"""
	path_length = 0
	origin = path[0]

	for destination in path[1:]:
		path_length += int(distances_table[distances_table.index == origin][destination])
		origin = destination

	return path_length


