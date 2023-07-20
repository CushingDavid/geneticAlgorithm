from helpers import word_select, output_results
from genetic_algorithm import genetic_algorithm


def admin_console():
    print("Admin Console")
    print("Current Constants:")
    for key, value in constants.items():
        print(f"{key}: {value}")

    while True:
        print("\nOptions:")
        print("1. Change Constant")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            constant_name = input("Enter the name of the constant to change: ")

            # Check if the constant exists and is valid for modification
            if constant_name in constants and constant_name not in ['GRID_SIZE', 'SUBGRID_SIZE', 'MAX_FITNESS']:
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
                        if 0.1 <= constant_value <= 1:
                            constants[constant_name] = constant_value
                            print("Constant changed successfully.")
                        else:
                            print("Crossover Rate and Mutation Rate should be between 0.1 and 1.")
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


def start_menu():
    print("Welcome to the Genetic Algorithm!")

    while True:
        print("\nStart Menu:")
        print("1. Run Genetic Algorithm")
        print("2. Admin Console")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            word = word_select()

            # Run the genetic algorithm and get the highest fitness child and score
            highest_fitness_child, highest_fitness_score = genetic_algorithm(constants, word)
            print("Genetic Algorithm completed.")

            # Output the results
            output_results(highest_fitness_child, highest_fitness_score)
        elif choice == '2':
            admin_console()
        elif choice == '3':
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Please try again.")


# Constants
constants = {
    'GRID_SIZE': 4,
    'SUBGRID_SIZE': 2,
    'POPULATION_SIZE': 1000,
    'SELECTED_POPULATION_SIZE': 500,
    'CROSSOVER_RATE': 0.8,
    'MUTATION_RATE': 0.5,
    'MAX_GENERATIONS': 800,
    'MAX_FITNESS': 24
}

# Start Menu
start_menu()
