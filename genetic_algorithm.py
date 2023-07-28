from initial_pop import create_initial_population
from helpers import write_fitness_scores_to_csv, find_highest_fitness_child

import numpy as np
import random
import multiprocessing


def genetic_algorithm(constants, word):
    # Create initial population
    population = create_initial_population(constants, word)
    print("\nPopulations created\nGenetic Algorithm starting...\n")

    max_fitness_solutions = set()
    highest_fitness_child = None
    highest_fitness_score = float('-inf')

    max_generations = constants['MAX_GENERATIONS']
    generation_thresholds = [10, 20, 30, 40, 50, 60, 70, 80, 90]  # Percentage thresholds

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        for generation in range(constants['MAX_GENERATIONS']):
            # Evaluate fitness for each individual in the population
            fitness_scores = pool.starmap(evaluate_fitness, [(constants, individual) for individual in population])

            # Write fitness scores and get the highest fitness child
            highest_fitness_child_current, highest_fitness_score_current = find_highest_fitness_child(fitness_scores,
                                                                                                      population)

            if highest_fitness_score_current > highest_fitness_score:
                highest_fitness_score = highest_fitness_score_current
                highest_fitness_child = highest_fitness_child_current

            if constants['WRITE_TO_CSV']:
                write_fitness_scores_to_csv(highest_fitness_child,
                                            highest_fitness_score_current,
                                            'fitness_scores.csv', )

            # Add highest fitness solution to set
            if highest_fitness_score_current == constants['MAX_FITNESS']:
                max_fitness_solutions.add(str(highest_fitness_child))

            if constants['ELITISM_ENABLED']:
                # Apply elitism by preserving a certain percentage of the fittest individuals
                num_elites = int(constants['ELITISM_RATE'] * constants['POPULATION_SIZE'])
                elite_indices = np.argsort(fitness_scores)[-num_elites:]
                elites = [population[i] for i in elite_indices]

                # Select best individuals as parents for the next generation (excluding elites)
                non_elite_indices = np.argsort(fitness_scores)[:-num_elites]
            else:
                # If elitism is not enabled, all individuals can be parents
                non_elite_indices = np.argsort(fitness_scores)
                elites = []

            # Select parents for the next generation
            selected_parents = [population[i] for i in non_elite_indices]

            # Create empty list for children
            children = []

            # Generate offspring through crossover
            for _ in range(constants['SELECTED_POPULATION_SIZE']):
                # select two parents randomly
                parent1 = random.choice(selected_parents)
                parent2 = random.choice(selected_parents)
                child = crossover(constants, parent1, parent2)
                children.append(child)

            # Mutate the children
            mutated_children = mutate(children, constants['MUTATION_RATE'], word)

            # Replace the population with mutated children and elites
            population = mutated_children + elites

            progress = (generation + 1) / max_generations * 100

            # Check and print progress at specific percentage thresholds
            for threshold in generation_thresholds:
                if progress == threshold:
                    print(f"Progress: {progress:.0f}% reached.")

    return highest_fitness_child, highest_fitness_score, max_fitness_solutions


def evaluate_fitness(constants, grid):
    fitness = 0
    unique_rows = set()
    unique_cols = set()
    unique_subgrids = set()

    # Check rows
    for row in grid:
        row_letters = [cell.lower() for cell in row if cell != '-']
        row_letters_str = ''.join(row_letters)
        if len(row_letters) != len(set(row_letters)) or row_letters_str in unique_rows:
            fitness -= 1
        else:
            fitness += 1
            unique_rows.add(row_letters_str)

    # Check columns
    for j in range(constants['GRID_SIZE']):
        column = [grid[i][j] for i in range(constants['GRID_SIZE'])]
        column_letters = [cell.lower() for cell in column if cell != '-']
        column_letters_str = ''.join(column_letters)
        if len(column_letters) != len(set(column_letters)) or column_letters_str in unique_cols:
            fitness -= 1
        else:
            fitness += 1
            unique_cols.add(column_letters_str)

    # Check subgroups
    for i in range(0, constants['GRID_SIZE'], constants['SUBGRID_SIZE']):
        for j in range(0, constants['GRID_SIZE'], constants['SUBGRID_SIZE']):
            subgrid_letters = []
            for x in range(i, i + constants['SUBGRID_SIZE']):
                for y in range(j, j + constants['SUBGRID_SIZE']):
                    letter = grid[x][y]
                    if letter != '-':
                        subgrid_letters.append(letter.lower())
            subgrid_letters_str = ''.join(subgrid_letters)
            if len(set(subgrid_letters)) == constants['SUBGRID_SIZE'] * constants['SUBGRID_SIZE'] \
                    and subgrid_letters_str not in unique_subgrids:
                fitness += 4
                unique_subgrids.add(subgrid_letters_str)
            else:
                fitness -= 4

    return fitness


def crossover(constants, parent1, parent2):
    child = [['-' for _ in range(constants['GRID_SIZE'])] for _ in range(constants['GRID_SIZE'])]

    for i in range(constants['GRID_SIZE']):
        for j in range(constants['GRID_SIZE']):
            # Skip crossover if the letter from parent1 is lowercase
            if parent1[i][j].islower():
                child[i][j] = parent1[i][j]
            else:
                if random.random() < constants['CROSSOVER_RATE']:
                    # Select gene from parent 1 if crossover occurs
                    child[i][j] = parent1[i][j]
                else:
                    # Select gene from parent 2 if crossover doesn't occur
                    child[i][j] = parent2[i][j]

    return child


def mutate(children, mutation_rate, word):
    for child in children:
        for i in range(len(child)):
            for j in range(len(child[i])):
                if child[i][j] == "-" or child[i][j].isupper():
                    if random.random() < mutation_rate:
                        valid_letters = [letter.upper() for letter in word]
                        # Mutate the gene by selecting a random letter from the valid letters
                        child[i][j] = random.choice(valid_letters)

    return children
