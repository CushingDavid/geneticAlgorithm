import ast
import csv


def word_select():
    # Prompt the user to enter a 4-letter word
    while True:
        res = input("Enter a 4-letter word to use: ").lower()

        # Check if the input is a valid 4-letter word consisting of letters only
        if len(res) == 4 and res.isalpha():
            return [x for x in res]  # Return the word as a list of letters
        else:
            print("Invalid input. Please enter a 4-letter word consisting of letters only.")


def set_initial_grid(constants, word, parent_num):
    # Create an initial grid filled with '-'
    grid = [['-' for _ in range(constants['GRID_SIZE'])] for _ in range(constants['GRID_SIZE'])]

    print(f"Please enter the initial grid for Parent {parent_num}.\n")

    # Iterate over each row and column
    for row in range(constants['GRID_SIZE']):
        for col in range(constants['GRID_SIZE']):
            valid_letter = False
            while not valid_letter:
                # Ask the user to enter a letter for the current position
                letter = input(f"Enter a letter for position ({row}, {col}) in Parent {parent_num}: ").lower()

                # Check if the input is a valid single letter from the word or '-'
                if len(letter) == 1 and (letter == '-' or letter in word):
                    grid[row][col] = letter  # Assign the letter to the current position in the grid
                    valid_letter = True
                else:
                    print("Invalid input. Please enter a single letter from the word or '-' to leave the cell empty.")

        # Print the current state of the grid for better visibility

        for r in grid:
            print('| ' + ' '.join(r) + ' |')

    print(f"Grid for Parent {parent_num} has been set.\n")

    return grid


def find_highest_fitness_child(fitness_scores, population):
    max_fitness_index = max(range(len(fitness_scores)), key=lambda i: fitness_scores[i])
    max_fitness_child = population[max_fitness_index]
    max_fitness_score = fitness_scores[max_fitness_index]

    return max_fitness_child, max_fitness_score


def write_fitness_scores_to_csv(child, score, output_file):

    with open(output_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([str(child), str(score)])


def output_results(highest_fitness_child, highest_fitness_score, max_fitness_solutions):
    # If max fitness solutions exist
    if max_fitness_solutions:
        print(f"\nMax Fitness Solutions: {len(max_fitness_solutions)}")
        for solution_str in max_fitness_solutions:
            solution = ast.literal_eval(solution_str)
            print_grid(solution)
            print()

    # If no max fitness solutions, print the highest fitness child
    else:
        print("\nNo Max Fitness Solution Found.")
        print("Highest Fitness Score: ", highest_fitness_score)
        print("Highest Fitness Child: ")
        print_grid(highest_fitness_child)


def print_grid(grid):
    # Prints the grid
    print("Grid:")
    for row in grid:
        print(row)



