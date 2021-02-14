import random
import numpy as np
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

def num_of_attacked_queens(state: State):
    n = 0
    board = state.data
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
    return 1.0/float(n)**4
    # return len(state.data) - n + 1

def generate_inital_population(lenght: int, n: int):
    population = []

    for _ in range(lenght):
        state = State(np.random.randint(low=n, size=n))
        ind = Node(state, adapt_func(state))
        population.append(ind)
    
    return population

def print_population(population: list, print_board: bool):
    for i, ind in enumerate(population):
        print("State:", ind.state, "Fitness Value:", ind.value)
        
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