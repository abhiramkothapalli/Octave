Octave: A Generative Music Engine using Genetic Algorithms and Markov Matrices

This repository contains the source code, sound samples, and the report.

Folder Overview:

graphs: contains several related graphs
matrices: contains saved matrices
samples: contains sound samples
Report: contains the report

Code Overview:

Dependencies:

pyaudio, numpy, matplotlib

Quickstart:

python3 playmarkov.py //To generate a new matrix
python3 playmarkov.py filename.npy //To use an existing matrix

Source Code Details:

generator.py: Contains the genetic algorithm process. Takes in population element constructor, crossover, mutate and fitness function as an argument. Also takes in number of generations, number of elements per population and exclusivity function.
markov.py: contains definitions for how to construct, crossover, and mutate a markov population element. Also contains the fitness function rule based on fitness.py
fitness.py: Contains various fitness functions that can be used and combined in markov.py
playmarkov.py: generates a markov matrix with specifications set in markov.py or takes an argument to an existing markov matrix. Plays the resulting Markov matrix.
