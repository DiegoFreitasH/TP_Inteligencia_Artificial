from structurs import *
import heapq
from typing import Tuple

def CHILD_NODE(problem: Problem, parent: Node, action: Action):
    state = problem.result(parent.state, action)
    if(state):
        return Node(state, parent, action, parent.path_cost + problem.step_cost(parent.state, action))
    return None

def IN_BORDER(border, state) -> Tuple[int, Node]:
    for i, (_, node) in enumerate(border):
        if(node.state == state):
            return i, node
    return None, None

def solution(node: Node) -> List[Node]:
    solution = []
    while(node.parent):
        solution.insert(0, node)
        node = node.parent
    solution.insert(0, node)
    return solution

def breath_first_search(problem: Problem) -> List[Node]:
    initial_node = Node(problem.initial_state, None, None, 0)

    border = []
    border.append(initial_node)

    explored = set()
    i = 0
    while(len(border) > 0 and i < 10**4):
        node = border.pop(0)

        if(problem.goal_test(node.state, problem.goal)):
            print(f"Num. of iterations: {i}")
            return solution(node)
        
        explored.add(node.state)

        for action in problem.actions:
            child = CHILD_NODE(problem, node, action)
            if(not child):
                continue
            if(child not in border and child not in explored):
                border.append(child)
        i += 1
    return None

def uniform_cost_search(problem: Problem) -> List[Node]:
    initial_node = Node(problem.initial_state, None, None, 0)

    border = PriorityQueue([(initial_node.path_cost, initial_node)])
    
    explored = set()

    i = 0
    while(not border.empty() and i < 1000):
        _, node = border.pop()

        if(problem.goal_test(node.state, problem.goal)):
            print(f"Num. Of Iterations: {i}")
            return solution(node)

        explored.add(node.state)
        
        for action in problem.actions:
            
            child = CHILD_NODE(problem, node, action)
            if(not child):
                continue
            
            border_pos, border_node = border.search(child.state)
            
            if(not border_node and child.state not in explored):
                border.push((child.path_cost ,child))
            
            elif(border_node and child.path_cost > border[border_pos][0]):
                border.replace(border_pos, (child.path_cost, child))
        
        i += 1
    return None

def evaluation_function(node: Node, heuristic):
    heuristic_value = heuristic(node.state)
    return heuristic_value + node.path_cost

def a_star_search(problem: Problem, heuristic) -> List[Node]:
    initial_node = Node(problem.initial_state, None, None, 0)

    border = []
    border = PriorityQueue([(initial_node.path_cost, initial_node)])
    
    explored = set()

    i = 0
    while(not border.empty() and i < 10**4):
        _, node = border.pop()

        if(problem.goal_test(node.state, problem.goal)):
            print(f"Num. Of Iterations: {i}")
            return solution(node)

        explored.add(node.state)
        
        for action in problem.actions:
            
            child = CHILD_NODE(problem, node, action)
            if(not child):
                continue
            
            child.h_value = heuristic(child.state)
            child.f_value = child.h_value + child.path_cost
            
            border_pos, border_node = border.search(child.state)
            
            if(not border_node and child.state not in explored):
                border.push((child.f_value ,child))
            
            elif(border_node and child.f_value > border.get(border_pos)[0]):
                border.replace(border_pos, (child.f_value, child))
        i += 1
    return None
