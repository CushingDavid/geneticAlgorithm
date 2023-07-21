from helpers import word_select, output_results
from genetic_algorithm import genetic_algorithm


def admin_console():
    print("Admin Console")
    print("Current Constants:")
    for key, value in constants.items():
        print(f"{key}: {value}")

    while True:
        print("\nOptions:")
        print("1. Change Value of a Constant")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            constant_name = input("Enter the name of the constant to change: ")

            # Check if the constant name is 'USER_INITIAL_GRID'
            if constant_name == 'USER_INITIAL_GRID':
                # Toggle
                constants[constant_name] = not constants[constant_name]
                print(f"Constant {constants[constant_name]} toggled successfully.")
            # Check if the constant exists and is valid for modification
            elif constant_name in constants and constant_name not in ['GRID_SIZE', 'SUBGRID_SIZE', 'MAX_FITNESS']:
                constant_value = input("Enter the new value: ")
                try:
                    constant_value = type(constants[constant_name])(constant_value)

                    if constant_name == 'SELECTED_POPULATION_SIZE':
                        # Check if the new value is valid for SELECTED_POPULATION_SIZE
                        if constant_value > constants['POPULATION_SIZE']:
                            print("Selected Population Size should not be bigger than Population Size.")
                        else:
                            constants[constant_name] = constant_value
                            print("Constant changed successfully.")
                    elif constant_name in ['CROSSOVER_RATE', 'MUTATION_RATE']:
                        # Check if the new value is within the valid range for CROSSOVER_RATE and MUTATION_RATE
                        if 0 <= constant_value <= 1:
                            constants[constant_name] = constant_value
                            print("Constant changed successfully.")
                        else:
                            print("Crossover Rate and Mutation Rate should be between 0 and 1.")
                    else:
                        constants[constant_name] = constant_value
                        print("Constant changed successfully.")
                except:
                    print("Invalid value entered.")
            else:
                print("Invalid constant name.")
        elif choice == '2':
            print("Exiting Admin Console.")
            break
        else:
            print("Invalid choice. Please try again.")


def explain_constants():
    print("\nExplanation of Constants:")
    print(f"\nGRID_SIZE ({constants['GRID_SIZE']}):"
          f" The size of the grid in the puzzle (e.g., 4 for a 4x4 grid).")
    print(f"\nSUBGRID_SIZE ({constants['SUBGRID_SIZE']}):"
          f" The size of the sub-grid in the puzzle (e.g., 2 for a 2x2 sub-grid).")
    print(f"\nUSER_INITIAL_GRID ({constants['USER_INITIAL_GRID']}):"
          f" Determines if the user will provide the initial grid or not.")
    print(f"\nPOPULATION_SIZE ({constants['POPULATION_SIZE']}):"
          f" The size of the population used in the genetic algorithm.")
    print(f"\nSELECTED_POPULATION_SIZE ({constants['SELECTED_POPULATION_SIZE']}):"
          f" The number of individuals selected for the next generation in the genetic algorithm.")
    print(f"\nCROSSOVER_RATE ({constants['CROSSOVER_RATE']}):"
          f" The probability of crossover happening between two individuals in the genetic algorithm.")
    print(f"\nMUTATION_RATE ({constants['MUTATION_RATE']}):"
          f" The probability of mutation happening in an individual in the genetic algorithm.")
    print(f"\nELITISM_RATE ({constants['ELITISM_RATE']}):"
          f" The percentage of the best individuals to be passed directly"
          f" to the next generation in the genetic algorithm.")
    print(f"\nMAX_GENERATIONS ({constants['MAX_GENERATIONS']}):"
          f" The maximum number of generations that the genetic algorithm will run for.")
    print(f"\nMAX_FITNESS ({constants['MAX_FITNESS']}): The maximum fitness score an individual can get.")


def start_menu():
    print("Welcome to the Genetic Algorithm!")
    print("\nThis program uses a genetic algorithm to solve a unique puzzle based on a user-selected word.")
    print(
        "The genetic algorithm is a search heuristic that is inspired by Charles Darwin's theory of natural evolution.")
    print("This algorithm reflects the process of natural selection where the fittest individuals "
          "are selected for reproduction.")
    print("The goal of the program is to evolve a population to get a grid with maximum fitness.\n")

    while True:
        print("\nStart Menu:")
        print("1. Run Base Genetic Algorithm")
        print("2. Run Genetic Algorithm with Elitism")
        print("3. Admin Console")
        print("4. Explanation of Constants")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            constants['ELITISM_ENABLED'] = False
            word = word_select()

            # Run the genetic algorithm and get the highest fitness child and score
            highest_fitness_child, highest_fitness_score = genetic_algorithm(
                constants, word)

            print("Genetic Algorithm completed.")
            # Output Results
            output_results(highest_fitness_child, highest_fitness_score)

        elif choice == '2':
            constants['ELITISM_ENABLED'] = True
            word = word_select()

            # Run the genetic algorithm and get the highest fitness child and score
            highest_fitness_child, highest_fitness_score = genetic_algorithm(
                constants, word)

            print("Genetic Algorithm with Elitism completed.")
            # Output Results
            output_results(highest_fitness_child, highest_fitness_score)

        elif choice == '3':
            admin_console()
        elif choice == '4':
            explain_constants()
        elif choice == '5':
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Please try again.")


# Constants
constants = {
    'GRID_SIZE': 4,
    'SUBGRID_SIZE': 2,
    'USER_INITIAL_GRID': False,
    'POPULATION_SIZE': 1000,
    'SELECTED_POPULATION_SIZE': 500,
    'CROSSOVER_RATE': 0.8,
    'MUTATION_RATE': 0.3,
    'ELITISM_ENABLED': False,
    'ELITISM_RATE': 0.1,
    'MAX_GENERATIONS': 10000,
    'MAX_FITNESS': 24
}


if __name__ == '__main__':
    start_menu()
