from enum import Enum
from typing import List
import heapq

class Action(Enum):
    RIGHT = 1
    LEFT = -1
    UP = -3
    DOWN = 3

class PriorityQueue:

    def __init__(self, data: list):
        self.data = data
        heapq.heapify(self.data)
    
    def get(self, index):
        return self.data[index]

    def push(self, item):
        heapq.heappush(self.data, item)
    
    def pop(self):
        return heapq.heappop(self.data)
    
    def empty(self):
        return len(self.data) == 0

    def search(self, state):
        for i, (_, node) in enumerate(self.data):
            if(node.state == state):
                return i, node
        return None, None
    
    def replace(self, index, item):
        self.data[index] = item
        heapq.heapify(self.data)

class State():
    
    def __init__(self, data: list, pos: int):
        self.data = data
        self.pos = pos

    def __repr__(self):
        return f"{self.data}"

    def __eq__(self, other):
        if(isinstance(other, State)):
            return self.data == other.data and self.pos == other.pos
        return False

    def __hash__(self):
        return hash(repr(self.data))

class Node():
    
    def __init__(self, state: State, parent, action: Action, path_cost: int):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.h_value = 0
        self.f_value = 0
    
    def __repr__(self):
        return f"State: {self.state} Cost: {self.path_cost} Action: {self.action}"

    def __lt__(self, other):
        return self.path_cost < other.path_cost

class Problem:

    def __init__(self, initial_state: State, actions: Enum, goal: State, trasition_model, goal_test, step_cost):
        self.initial_state = initial_state
        self.actions = actions
        self.result = trasition_model
        self.goal = goal
        self.goal_test = goal_test
        self.step_cost = step_cost
