#!/usr/bin/env python

import random
import numpy as np
import matplotlib.pyplot as plt

#generates our first set of candidates
def initalize(constructor, N):
    start_generation = []
    for n in range(N):
        start_generation.append(constructor())
    return start_generation

#gives us a weighted_choice of an element from candidates
def weighted_choice(candidates, weights):
    r = random.uniform(0, 1)
    total = 0
    for i in range(len(weights)):
        w = weights[i]
        total = total + w
        if total >= r:
            return candidates[i]

#generates a new set of candidates based on selected generation
def iterate(generation, N, mutate, crossover, fitness, exclusivity):
    candidates = selector(generation, fitness, exclusivity)

    fitness_scores = [fitness(x) for x in candidates]
    total = float(sum(fitness_scores))
    weights = [float(x) / float(total) for x in fitness_scores]
    
    new_generation = []
    #selection
    for i in range(N):
        #randomly pick two parents
        parent1 = weighted_choice(candidates, weights)
        parent2 = weighted_choice(candidates, weights)

        #perform genetic operations
        child = mutate(crossover(parent1 , parent2))
        new_generation.append(child)

    return new_generation

#selects a subgroup of the population based on generation
#TODO error here
def selector(generation, fitness, exclusivity):
    return sorted(generation, key=fitness)[int(len(generation) * (1 - exclusivity)):]




def graph(fit_array):
    plt.figure()
    plt.plot(np.arange(0, len(fit_array)), fit_array)
    plt.xlabel("Generation")
    plt.xlabel("Fitness")
    plt.title("Matrix Fitness over Time N=10000, mutation_prob=0.01, exclusivity=0.01")
    plt.show()

#runs our genetic algorithm
#constructor(): returns an element of a generation
#crossover(a, b): mixes the result of a and b
#mutate(a): randomly changes a
#fitness(a): evaluates the fitness of a
#N: total number of elements per generation
#K: total number of iterations
#exclusivity: proportion of population selected to be candidate pool
def generate(constructor, crossover, mutate, fitness, N, K, exclusivity):
    fit_array = []
    generation = initalize(constructor, N)
    fit = max([fitness(x) for x in generation])
    print("Seed Generation Fitness: "+ str(fit))
    fit_array.append(fit)
    for i in range(K):
        generation = iterate(generation, N, mutate, crossover, fitness, exclusivity)
        fit = max([fitness(x) for x in generation])
        fit_array.append(fit)
        print("Generation " + str(i + 1) + "/" + str(K)  + " Fitness: "+ str(fit))

    graph(fit_array)
    return sorted(generation, key=fitness)[-1]
