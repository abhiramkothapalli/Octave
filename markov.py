#!/usr/bin/env python
from generator import generate
import random
import numpy as np
from fitness import *


#constructs a random order o transition matrix
def constructor():
    a = (10 * np.random.rand(size ** order, size)) ** 2
    #a = np.random.rand(size ** order, size)

    '''
    a = np.zeros((size ** order, size))
    for i in range(size ** order):
        a[i] = np.zeros((size))
        for k in range(3):
            r = random.randint(0, size - 1)
            a[i][r] = random.uniform(0, 1)
    '''
                
    return a / a.sum(axis=1)[:, np.newaxis]

def crossover(a, b):

    split_point = random.randint(0, (size ** order) - 1)

    final  = np.zeros((size ** order, size))
    for i in range(size ** order):
        if i < split_point:
            final[i] = a[i]
        else:
            final[i] = b[i]
    return final

def mutate(a):
    for i in range(size ** order):
        for j in range(size):
            r = random.uniform(0, 1)
            if r < mutation_prob:
                #assign a new probability
                a[i][j] = random.uniform(0, 1)
    return a / a.sum(axis=1)[:, np.newaxis]

def fitness(a):

    total = 0

    total += jump(a)
    #total += reverse_descension(a)
    #total += reverse_ascension(a)
    total += long_notes(a)
    #total += descension(a)
    #total += ascension(a) * 2
    #total += less_pause(a)
    #total += more_pause(a)
    #total += rand(a)

    return total
    
#parameters
size = 7
order = 1
mutation_prob = 0.1
N = 1000
K = 35
exclusivity = 0.01

def create_markov():
    print("Initalizing an order " + str(order) + " Markov matrix...")
    markov = generate(constructor, crossover, mutate, fitness, N, K, exclusivity)
    print("Finished evolution, playing composition...")
    print(markov)
    return markov


