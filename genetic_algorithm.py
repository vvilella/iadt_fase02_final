import random
from typing import List

# Default population size used in selection
population_size = 100


def selection(population: List[List[float]], fitness_values: List[float]) -> List[List[float]]:
    """Select individuals from the population using roulette wheel sampling."""
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    indices = random.choices(range(population_size), weights=probabilities, k=population_size)
    return [population[i] for i in indices]


def mutation(portfolio: List[float]) -> List[float]:
    """Mutate a portfolio by changing one weight and renormalizing."""
    idx = random.randrange(len(portfolio))
    portfolio = portfolio.copy()
    portfolio[idx] = random.random()
    total = sum(portfolio)
    return [w / total for w in portfolio]
