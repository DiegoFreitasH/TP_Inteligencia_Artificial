import random
import numpy as np
from lib import *
from structurs import *

def num_of_attacked_queens(state: State):
    n = 0
    board = state.data

    for i, pos in enumerate(board):
        for x_1, y_1 in enumerate(board):
            if(i == x_1):
                continue
            if(y_1 == pos or abs(y_1 - pos) == abs(x_1 - i)):
                n += 1
                break

    return n

def adapt_func(state: State):
    n = num_of_attacked_queens(state)

    # if(n == 0):
        # return float("infinity")
    # return 1.0/float(n)
    return len(state.data) - n + 1

def generate_inital_population(lenght: int, n: int):
    population = []

    for _ in range(lenght):
        state = State([np.random.randint(low=n) for _ in range(n)])
        ind = Node(state, adapt_func(state))
        population.append(ind)
    
    return population

def print_population(population: list, print_board: bool):
    for i, ind in enumerate(population):
        print("State:", ind.state, "Fitness Value:", ind.value-1)
        
        if(print_board):
            for j in range(len(ind.state.data)):
                for k in range(len(ind.state.data)):
                    if(ind.state.data[k] == j):
                        print("|X|", end='')
                    else:
                        print("| |", end='')
                print()
            print()

def main():
    
    board_size = 40
    population_size = 300
    population = generate_inital_population(population_size, board_size)

    weights = [ind.value for ind in population]
    solution = genetic_algorithm(population, weights, 0.3, adapt_func, 1500, board_size)

    print_population([solution], False)

if __name__ == '__main__':
    main()