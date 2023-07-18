import random


def create_initial_population(constants, word):
    """
    parent1 = [['w','d','r','o'],['o','r','w','d'],['r','o','d','w'],['d','w','o','r']]
    parent2 = [['w','d','r','o'],['o','r','w','d'],['r','o','d','w'],['d','w','o','r']]

    parent1 = [['w','','','o'],
           ['o','r','','d'],
           ['r','','',''],
           ['','','o','r']]
    parent2 = [['w','','r','o'],
           ['','r','w','d'],
           ['r','','d','w'],
           ['d','w','o','r']]
    """
    population = []
    for _ in range(constants['POPULATION_SIZE']):
        individual = [['-' for _ in range(constants['GRID_SIZE'])] for _ in range(constants['GRID_SIZE'])]
        total_slots = constants['GRID_SIZE'] * constants['GRID_SIZE']
        num_mutations = int(constants['MUTATION_RATE'] * total_slots)
        mutation_indices = random.sample(range(total_slots), num_mutations)

        for index in mutation_indices:
            row = index // constants['GRID_SIZE']
            col = index % constants['GRID_SIZE']
            random_word = random.choice(word)
            individual[row][col] = random_word.lower()

        population.append(individual)

    return population
