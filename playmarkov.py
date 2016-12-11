#!/usr/bin/env python
from generator import generate
from markov import create_markov
import time
import math
import numpy
from numpy.random import choice
import pyaudio
from threading import Thread

notes = {}
#western scale
'''
marnotes[0] = 260.00 #261.63 #C
notes[1] = 290.00 #293.66 #D
notes[2] = 330.00 #329.63 #E
notes[3] = 350.00 #349.23 #F
notes[4] = 390.00 #392.00 #G
notes[5] = 440.00 #440.00 #A
notes[6] = 490.00 #493.88 #B
notes[7] = 520.00 #523.25 #C
'''


#pentatonic scale
'''
notes[0] = 260.00#C
notes[1] = 330.00#E
notes[2] = 370.00#F#
notes[3] = 390.00#G
notes[4] = 490.00#B
notes[5] = 520.00#C
'''
'''
notes[6] = 660.00#E
notes[7] = 740.00#F#
notes[8] = 780.00#G
notes[9] = 990.00#B
notes[10] = 1050.00#C
'''

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
#stream.close()
#p.terminate()

def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)

#rate=44100
def play_tone(frequency, stream=stream, length=0.30, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))
    chunk = numpy.concatenate(chunks) * 0.25
    stream.write(chunk.astype(numpy.float32).tostring())

def save(markov):
    numpy.save("./matrices/markov", markov)

def load(filename):
    return numpy.load("./matrices/markov.txt.npy")

def get_state(order_array, note_num):

    current = 0
    for i in range(len(order_array)):
        p = len(order_array) - 1 - i
        current = (note_num ** p) * order_array[i]
    return current

    
def play_stream(markov):

    print("Saving file...")
    save(markov)

    size, note_num = markov.shape
    order = int(math.log(size, note_num))
    order_array = [0 for x in range(order)]
    
    current = 0
    index_array = numpy.arange(note_num)

    
    
    while(True):
        #plays the tone
        play_tone(notes[current])

        #picks next note based on distribution
        current = choice(index_array, p=markov[get_state(order_array, note_num)])

        #updates order array
        order_array.append(current)
        order_array.pop(0)

        
def test_notes():
    for k in range(100):
        for i in range(len(notes)):
            play_tone(notes[i])


#test_notes()            
markov = create_markov()
play_stream(markov)


