import argparse
from enum import Enum
from typing import List
from structurs import *
from lib import *

def switch(puzzle, i, j):
    puzzle[i], puzzle[j] = puzzle[j], puzzle[i]
    return puzzle

def puzzle_trasition(state: State, action: Action):
    pos = state.pos

    if((action == Action.RIGHT or Action.LEFT) and 0 <= (pos%3)+action.value < 3):
        end_pos = pos + action.value
    elif((action == Action.UP or Action.DOWN) and 0 <= pos+action.value < 9):
        end_pos = pos + action.value
    else:
        return None
    
    puzzle_list = state.data.copy()
    puzzle_list = switch(puzzle_list, pos, end_pos)
    new_state = State(puzzle_list, end_pos)
    return new_state

def puzzle_goal_test(state: State, goal: State):
    return state == goal

def puzzle_step_cost(state: State, action: Action):
    return 1

def h_pieces_out_of_place(state: State) -> int:
    goal = [1,2,3,4,5,6,7,8,0]
    value = 0
    for i in range(8):
        if(goal[i] != state.data[i]):
            value += 1
    return value

def main(puzzle, algorithm):
    goal = State([1,2,3,4,5,6,7,8,0], 8)

    initial_state = State(
        puzzle,
        puzzle.index(0)
    )

    puzzle_problem = Problem(initial_state, Action, goal, puzzle_trasition, puzzle_goal_test, puzzle_step_cost)
    
    if(algorithm == 'bfs'):
        result = breath_first_search(puzzle_problem)
    elif(algorithm == 'a_star'):
        result = a_star_search(puzzle_problem, h_pieces_out_of_place)
    else:
        raise ValueError("Invalid Algorithm Name")
    

    if(result):
        print("Solution: ")
        for node in result:
            print(f"\t{node}")
    else:
        print("No Solution Found")

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument(
        'algorithm',
        choices=['bfs', 'a_star'],
        help='Name of the algorithm'
    )
    parser.add_argument(
        "puzzle",
        metavar="puzzle",
        type=str,
        help='List of piece positions, where 0 is the empty position'
    )
    
    args = parser.parse_args()
    puzzle: str = args.puzzle
    algo = args.algorithm
    
    puzzle = [int(n) for n in puzzle.strip()[1:-1].split(',')]

    main(puzzle, algo)
    
