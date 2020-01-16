import numpy as np
from solve_K import *



def read_A_matrix(input_file):
    # with open(input_file, "r") as f:
    #     f1 = f.splitline()
    #     print f1
    file = open(input_file,'r').read().splitlines()
    A = []
    for line in file:
        new_line = []
        line = line.split()
        for el in line:
            el = float(el)
            new_line.append(el)
        A.append(new_line)
    return A

A = read_A_matrix('A2.txt')
print A
print A_list
