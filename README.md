# Genetic Algorithm Puzzle Solver

[![Build Status](https://img.shields.io/badge/build-passing-green)](https://github.com/DeeK-Dev/geneticAlgorithm)

This is a Python project implementing a genetic algorithm to solve a grid-based puzzle. The objective of the puzzle is to fill a grid of size 4x4 with four different letters, sourced from a user-selected 4-letter word, so that each column, each row, and each of the four sub-grids of size 2x2 contain each of the four letters only once. 

The genetic algorithm optimizes the configuration of letters in the grid by performing operations of selection, crossover, mutation, and optionally elitism, iteratively over a specified number of generations.

## Prerequisites

- Python 3.x installed on your system

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/DeeK-Dev/geneticAlgorithm.git
```

Move to the cloned directory:

```bash
cd geneticAlgorithm
```

## Running the Program

Start the program with the command:

```bash
python main.py
```

When you run the program, it will first prompt you to enter a 4-letter word. This word will determine the letters used in the grid.

## Constants

The behavior of the genetic algorithm is determined by several constants. Here is a brief overview of their meanings:

- `GRID_SIZE` : The size of the grid in the puzzle (e.g., 4 for a 4x4 grid).
- `SUBGRID_SIZE` : The size of the sub-grid in the puzzle (e.g., 2 for a 2x2 sub-grid).
- `USER_INITIAL_GRID` : Determines if the user will provide the initial grid or not.
- `POPULATION_SIZE` : The size of the population used in the genetic algorithm.
- `SELECTED_POPULATION_SIZE` : The number of individuals selected for the next generation in the genetic algorithm.
- `CROSSOVER_RATE` : The probability of crossover happening between two individuals in the genetic algorithm.
- `MUTATION_RATE` : The probability of mutation happening in an individual in the genetic algorithm.
- `ELITISM_ENABLED` : Determines whether or not the elitism is enabled. If true, a percentage of the best individuals will be passed directly to the next generation.
- `ELITISM_RATE` : The percentage of the best individuals to be passed directly to the next generation in the genetic algorithm.
- `MAX_GENERATIONS` : The maximum number of generations that the genetic algorithm will run for.
- `MAX_FITNESS` : The maximum fitness score an individual can get.

You can alter these constants to tune the genetic algorithm's behavior as per your requirements.

## Contributing

We are open to contributions. Please submit a pull request if you would like to contribute to this project.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
