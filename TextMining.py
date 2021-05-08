import os

import form as form
from matplotlib import pyplot as plt

def countWords(file):
    words = {}
    for line in file:
        w = line.split(" ")  # output list
        for b in line.split():
            words[b] = words.get(b, 0) + 1

        for w, c in words.items():
            print
file = open("mytext.txt", "r")
countWords(fileitem.filename)
