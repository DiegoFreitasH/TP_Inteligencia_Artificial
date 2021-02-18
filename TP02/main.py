import random
import argparse
import numpy as np
from numba import jit
from lib import *
from structurs import *

def queens_actions(state: State):
    actions = []
    board_size = len(state.data)
    for i in range(board_size):
        if(state.data[i] == 0):
            actions.append([i, Action.DOWN])
        elif(state.data[i] == board_size - 1):
            actions.append([i, Action.UP])
        else:
            actions.append([i, Action.UP])
            actions.append([i, Action.DOWN])
    return actions

def queens_transition(state: State, action):
    i, move = action
    new_state = State(state.data.copy())
    new_state.data[i] += move.value
    return new_state

@jit(nopython=True)
def num_of_attacked_queens(board: list):
    n = 0

    is_attacked = [False for i in range(len(board))]

    for x, y in enumerate(board):

        if(is_attacked[x]):
            continue

        for x_1, y_1 in enumerate(board[x+1:], x+1):
            
            if(y == y_1 or abs(y_1 - y) == abs(x_1 - x)):
                if(not is_attacked[x_1]): n += 1
                is_attacked[x] = True
                is_attacked[x_1] = True
        
        if(is_attacked[x]):
            n += 1

    return n

def adapt_func(state: State):
    n = num_of_attacked_queens(state)

    if(n == 0):
        return float("infinity")
    else:
        return 1.0/2**float(n)

def generate_inital_population(lenght: int, n: int):
    population = []

    for _ in range(lenght):
        state = State(np.random.randint(low=n, size=n))
        ind = Node(state, adapt_func(state.data))
        population.append(ind)
    
    return population

def print_population(population: list, print_board: bool):
    for _, ind in enumerate(population):
        print("State:", ind.state)
        print("Fitness Value:", ind.value)
        print("Num. Attacked Queens:", num_of_attacked_queens(ind.state.data))
        
        if(print_board):
            for j in range(len(ind.state.data)):
                for k in range(len(ind.state.data)):
                    if(ind.state.data[k] == j):
                        print("|X|", end='')
                    else:
                        print("| |", end='')
                print()
            print()

def main(population_size=500, board_size=40, mutability=0.4, max_generations=1500):
    
    population = generate_inital_population(population_size, board_size)

    weights = [ind.value for ind in population]
    solution = genetic_algorithm(population, weights, mutability, adapt_func, max_generations, board_size, DEBUG=True)

    print("Solution: ")
    print_population([solution], False)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Program to solve the queens puzzle. The higher the fitness value the closer to a solution. Solution have fitness value of 'inf'"
    )

    parser.add_argument(
        '--population-size',
        metavar='p_size',
        default=300,
        type=int,
        required=False,
        help='Size of the population per generation'
    )
    parser.add_argument(
        '--board-size',
        metavar='b_size',
        default=40,
        type=int,
        required=False,
        help='Size of the board'
    )
    parser.add_argument(
        '--mutability',
        default=0.4,
        type=float,
        required=False,
        help='Rate of mutation'
    )
    parser.add_argument(
        '--max-generation',
        default=float('infinity'),
        type=int,
        required=False,
        help='Max number of generations'
    )

    args = parser.parse_args()

    population_size = args.population_size
    board_size = args.board_size
    mutability = args.mutability
    max_generation = args.max_generation

    main(population_size, board_size, mutability, max_generation)