#!/usr/bin/env python

import numpy as np
import random

#Contains a list of fitness functions


def rand(a):
    return random.uniform(0,1)

def ascension(a):
    return sum(np.diag(a, 1))

def descension(a):
    return sum(np.diag(a, -1))

def long_notes(a):
    return sum(np.diag(a))

def hold(a, note):
    return a[note][note]

def jump(a):
    return sum(np.diag(np.fliplr(a)))

def reverse_ascension(a):
    return sum(np.diag(np.fliplr(a), 1))

def reverse_descension(a):
    return sum(np.diag(np.fliplr(a), -1))

def less_pause(a):
    x, y = a.shape
    return -sum(a[:, y - 1])

def more_pause(a):
    x, y = a.shape
    return sum(a[:, y - 1])
