import os
import sys
import random

# ensure parent directory is on path when running via pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import genetic_algorithm as ga


def test_selection_returns_same_length():
    population_size = 5
    population = [[random.random() for _ in range(3)] for _ in range(population_size)]
    population = [[w / sum(p) for w in p] for p in population]
    fitness = [float(i + 1) for i in range(population_size)]

    ga.population_size = population_size
    selected = ga.selection(population, fitness)

    assert isinstance(selected, list)
    assert len(selected) == population_size


def test_mutation_normalizes_weights():
    portfolio = [0.2, 0.3, 0.5]
    mutated = ga.mutation(portfolio)
    assert abs(sum(mutated) - 1.0) < 1e-9
