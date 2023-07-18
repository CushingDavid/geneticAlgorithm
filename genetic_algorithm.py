from initial_pop import create_initial_population
from helpers import write_fitness_scores_to_csv

import numpy as np
import random


def genetic_algorithm(constants, word):
    # Create initial population
    population = create_initial_population(constants, word)

    highest_fitness_child = None
    highest_fitness_score = float('-inf')

    for generation in range(constants['MAX_GENERATIONS']):
        # Evaluate fitness for each individual in the population
        fitness_scores = [evaluate_fitness(constants, individual, word) for individual in population]

        # Write fitness scores and get the highest fitness child
        highest_fitness_child, highest_fitness_score = write_fitness_scores_to_csv(fitness_scores,
                                                                                   population,
                                                                                   'fitness_scores.csv')

        # Check termination condition
        if constants['MAX_FITNESS'] in fitness_scores:
            break

        # Select best individuals as parents for the next generation
        selected_indices = np.argsort(fitness_scores)[-constants['SELECTED_POPULATION_SIZE']:]
        selected_parents = [population[i] for i in selected_indices]

        # Create empty list for children
        children = []

        # Generate offspring through crossover
        for _ in range(constants['SELECTED_POPULATION_SIZE']):
            child = crossover(constants, selected_parents[0], selected_parents[1])
            children.append(child)

        # Mutate the children
        mutated_children = mutate(children, constants['MUTATION_RATE'], word)

        # Replace the population with mutated children
        population = mutated_children

    return highest_fitness_child, highest_fitness_score


def evaluate_fitness(constants, grid, word):
    fitness = 0

    # Check rows
    for row in grid:
        if all(cell in word for cell in row):
            fitness += 1

    # Check columns
    for j in range(constants['GRID_SIZE']):
        column = [grid[i][j] for i in range(constants['GRID_SIZE'])]
        if all(cell in word for cell in column):
            fitness += 1

    # Check subgroups
    for i in range(0, constants['GRID_SIZE'], constants['SUBGRID_SIZE']):
        for j in range(0, constants['GRID_SIZE'], constants['SUBGRID_SIZE']):
            subgrid_letters = []
            for x in range(i, i + constants['SUBGRID_SIZE']):
                for y in range(j, j + constants['SUBGRID_SIZE']):
                    letter = grid[x][y]
                    if letter in subgrid_letters:
                        fitness -= 2  # Decrease fitness if a letter is repeated in the subgrid
                    subgrid_letters.append(letter.upper())

            if len(set(subgrid_letters)) == constants['SUBGRID_SIZE'] * constants['SUBGRID_SIZE']:
                fitness += 4  # Add 4 to fitness if subgrid_letters has 4 unique elements

    return fitness


def crossover(constants, parent1, parent2):
    child = [['-' for _ in range(constants['GRID_SIZE'])] for _ in range(constants['GRID_SIZE'])]

    for i in range(constants['GRID_SIZE']):
        for j in range(constants['GRID_SIZE']):
            if random.random() < constants['CROSSOVER_RATE']:
                child[i][j] = parent1[i][j]
            else:
                child[i][j] = parent2[i][j]

    return child


def mutate(children, mutation_rate, word):
    for child in children:
        for i in range(len(child)):
            for j in range(len(child[i])):
                if child[i][j] == "-" or child[i][j].isupper():
                    if random.random() < mutation_rate:
                        valid_letters = [letter.upper() for letter in word]
                        child[i][j] = random.choice(valid_letters)

    return children
