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


def set_initial_grid(constants, word):
    # Create an initial grid filled with '-'
    grid = [['-' for _ in range(constants['GRID_SIZE'])] for _ in range(constants['GRID_SIZE'])]

    # Prompt the user to enter letters for each position in the grid
    for i in range(constants['GRID_SIZE']):
        for j in range(constants['GRID_SIZE']):
            while True:
                # Ask the user to enter a letter for the current position
                letter = input(f"Enter a letter for position ({i}, {j}): ").lower()

                # Check if the input is a valid single letter from the word or '-'
                if len(letter) == 1 and (letter == '-' or letter in word):
                    grid[i][j] = letter  # Assign the letter to the current position in the grid
                    break
                else:
                    print("Invalid input. Please enter a single letter from the word or '-' to leave the cell empty.")

    return grid


def write_fitness_scores_to_csv(fitness_scores, children, output_file):
    # Find the index of the child with the highest fitness score
    max_fitness_index = max(range(len(fitness_scores)), key=lambda i: fitness_scores[i])

    # Retrieve the child and fitness score with the highest fitness
    max_fitness_child = children[max_fitness_index]
    max_fitness_score = fitness_scores[max_fitness_index]

    # Write the fitness scores and corresponding children to a CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Child', 'Fitness Score'])
        for i in range(len(fitness_scores)):
            writer.writerow([str(children[i]), str(fitness_scores[i])])

    return max_fitness_child, max_fitness_score


def output_results(highest_fitness_child, highest_fitness_score):
    # Print the highest fitness child and score
    print(f"Highest Fitness Child: {highest_fitness_child}")
    print(f"Highest Fitness Score: {highest_fitness_score}")
    print("Grid:")

    # Print the grid of the highest fitness child
    for row in highest_fitness_child:
        print(row)
