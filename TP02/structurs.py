from enum import Enum
import numpy as np

class Action(Enum):
    UP = -1
    DOWN = 1

class State:
    def __init__(self, data: np.ndarray):
        self.data = data

    def __repr__(self):
        return f"{self.data}"

    def __eq__(self, other):
        if(isinstance(other, State)):
            return self.data == other.data
        return False

    def __hash__(self):
        return hash(repr(self.data))

class Node:

    def __init__(self, state: State, value: float):
        self.state = state
        self.value = value
    
    def __repr__(self):
        return f"State: {self.state} Value: {self.value}"

    def __lt__(self, other: State):
        return self.value < other.value

class Problem:
    
    def __init__(self, initial_state: State, actions: Enum, trasition_model, eval_function):
        self.initial_state = initial_state
        self.actions = actions
        self.result = trasition_model
        self.eval_function = eval_function
