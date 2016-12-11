#!/usr/bin/env python

import numpy as np

#Contains a list of fitness functions


def ascension(a):
    return sum(np.diag(a, 1))

def descension(a):
    return sum(np.diag(a, -1))

def long_notes(a):
    return sum(np.diag(a))

def hold(a, note):
    return a[note][note]
