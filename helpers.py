import csv


def word_select():
    while True:
        res = input("Enter a 4-letter word to use: ").lower()
        if len(res) == 4 and res.isalpha():
            return [x for x in res]
        else:
            print("Invalid input. Please enter a 4-letter word consisting of letters only.")


def set_initial_grid(constants, word):
    grid = [['-' for _ in range(constants['GRID_SIZE'])] for _ in range(constants['GRID_SIZE'])]

    for i in range(constants['GRID_SIZE']):
        for j in range(constants['GRID_SIZE']):
            while True:
                letter = input(f"Enter a letter for position ({i}, {j}): ").lower()
                if len(letter) == 1 and (letter == '-' or letter in word):
                    grid[i][j] = letter
                    break
                else:
                    print("Invalid input. Please enter a single letter from the word or '-' to leave the cell empty.")

    return grid


def write_fitness_scores_to_csv(fitness_scores, children, output_file):
    max_fitness_index = max(range(len(fitness_scores)), key=lambda i: fitness_scores[i])
    max_fitness_child = children[max_fitness_index]
    max_fitness_score = fitness_scores[max_fitness_index]

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Child', 'Fitness Score'])
        for i in range(len(fitness_scores)):
            writer.writerow([str(children[i]), str(fitness_scores[i])])

    return max_fitness_child, max_fitness_score


def check_termination_condition(max_fitness, fitness_scores):
    return max_fitness in fitness_scores


def output_results(highest_fitness_child, highest_fitness_score):
    print(f"Highest Fitness Child: {highest_fitness_child}")
    print(f"Highest Fitness Score: {highest_fitness_score}")
    print("Grid:")
    for row in highest_fitness_child:
        print(row)
