import random


def create_initial_population(constants, word):
    population = []

    # Generate individuals for the population
    for _ in range(constants['POPULATION_SIZE']):
        # Create an individual grid filled with '-'
        individual = [['-' for _ in range(constants['GRID_SIZE'])] for _ in range(constants['GRID_SIZE'])]

        # Calculate the total number of cells in the grid
        total_slots = constants['GRID_SIZE'] * constants['GRID_SIZE']

        # Calculate the number of cells to mutate based on the mutation rate
        num_mutations = int(constants['MUTATION_RATE'] * total_slots)

        # Randomly select indices to undergo mutation
        mutation_indices = random.sample(range(total_slots), num_mutations)

        # Assign random letters to the selected mutation indices
        for index in mutation_indices:
            # Calculate the row and column indices for the current index
            row = index // constants['GRID_SIZE']
            col = index % constants['GRID_SIZE']

            # Assign a randomly chosen lowercase letter from the 'word' list to the cell
            random_word = random.choice(word)
            individual[row][col] = random_word.lower()

        # Add the individual to the population
        population.append(individual)

    return population

