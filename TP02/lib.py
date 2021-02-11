from structurs import *
import math
import random
import operator
import numpy as np

def CREATE_NODE(state: State, problem):
    pass

def annealing_schedule(t: int):
    pass

def simulated_annealing(problem: Problem):
    pass

def random_selection(population, adapt_func) -> State:
    fitness_sum = 0
    partial_sum = 0

    for ind in population:
        fitness_sum += ind.value

    wheel = np.random.randint(low=1, high=fitness_sum+1)
    
    i = np.random.randint(low=len(population))
    while(partial_sum < wheel):
        if(i >= len(population)):
            i = 0
        partial_sum += population[i].value
        i += 1
    
    return population[i-1] 

def reproduction(x: State, y: State) -> State:
    cross_point = np.random.randint(low=1, high=len(x.data)-1)
    x_gene = x.data[:cross_point]
    y_gene = y.data[cross_point:]

    child = State(x_gene + y_gene)
    
    return child

def mutation(child: State) -> State:
    pos = np.random.randint(low=len(child.data))
    value = np.random.randint(low=len(child.data))


    child.data[pos] = value
    return child

def genetic_algorithm(population: list, weights: list, multability, adapt_func, num_of_iter=10, solution_threshold=None):
    
    keep_n = len(population)//10

    for i in range(num_of_iter):

        new_population = []

        # Keep [keep_n] indviduos of the last generation
        new_population.extend(random.choices(population, weights=weights, k=keep_n-len(new_population)))

        if(True):
            print("Iter:",i)
            print("  Population:",len(population)) 
            print("  Childs:",len(population) - keep_n)
            print("  Parents:", keep_n)
            print("  Parents Fitness:", [p.value-1 for p in new_population])
            best_child = max(population, key=lambda x: x.value)
            print("  Best Child:", best_child.value-1)
        
        # Decreases the mutability be the end of the algorithm
        if(i > 2*num_of_iter//3):
            multability *= 0.1
        
        for k in range(len(population) - keep_n):

            x = random.choices(population, weights=weights)[0]
            y = random.choices(population, weights=weights)[0] 

            child_state = reproduction(x.state, y.state)
            
            if(np.random.random() <= multability):
                child_state = mutation(child_state)
            
            child = Node(child_state, adapt_func(child_state))

            if(solution_threshold and child.value >= solution_threshold):
                return child
            
            new_population.append(child)
        
    
        population = new_population[:]
        weights = [indv.value for indv in population]

    best_child = max(population, key=lambda x: x.value)
    return best_child

