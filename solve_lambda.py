import numpy as np
from params import *

#Klasa 1
A_list =[
    [-1, 0, 0, 0, 0],
    [0.6, -1, 0, 0, 0],
    [0.3, 0.9, -1, 0.05, 0.05],
    [0.05, 0.05, 0.5, -1, 0],
    [0.05, 0.05, 0.5, 0, -1],
]
b_list = [[-lam_0_1], [0],[0],[0],[0]]
A = np.array(A_list)
b = np.array(b_list)
lam_1 = np.linalg.inv(A).dot(b)
lam_1 = [el[0] for el in lam_1]

print "\n"
print "Klasa 1"
print "Lambda"
print lam_1

#Klasa 2
A_list =[
    [0.1, 0.1, 1, -1],
    [0.6, -1, 0, 0],
    [0.3, 0.9, -1, 0.1],
    [1, 0, 0, 0]
]
b_list = [[0],[0],[0],[lam_0_2]]

A = np.array(A_list)
b = np.array(b_list)
lam_2 = np.linalg.inv(A).dot(b)
lam_2 = [el[0] for el in lam_2]
print "\n"
print "Klasa 2"
print "Lambda"
print lam_2

#Klasa 3
A_list =[
    [0.1, 0.1, 1, -1],
    [0.6, -1, 0, 0],
    [0.3, 0.9, -1, 0.1],
    [1, 0, 0, 0]
]
b_list = [[0],[0],[0],[lam_0_3]]

A = np.array(A_list)
b = np.array(b_list)
lam_3 = np.linalg.inv(A).dot(b)
lam_3 = [el[0] for el in lam_3]
print "\n"
print "Klasa 3"
print "Lambda"
print lam_3


#Klasa 4
A_list = [
    [1, -1],
    [1, 0]
]
b_list = [[0], [lam_0_4]]

A = np.array(A_list)
b = np.array(b_list)
lam_4 = np.linalg.inv(A).dot(b)
lam_4 = [el[0] for el in lam_4]
print "\n"
print "Klasa 4"
print "Lambda"
print lam_4

#Klasa 5
A_list = [
    [1, -1],
    [1, 0]
]
b_list = [[0], [lam_0_5]]

A = np.array(A_list)
b = np.array(b_list)
lam_5 = np.linalg.inv(A).dot(b)
lam_5 = [el[0] for el in lam_5]
print "\n"
print "Klasa 5"
print "Lambda"
print lam_5

print "\n"

# lambda[system][klasa]
lam = {
    1 : { 1: lam_1[0], 2: lam_2[0], 3: lam_3[0], 4: lam_4[0], 5: lam_5[0]},
    2 : { 1: lam_1[1], 2: lam_2[1], 3: lam_3[1], 4: None, 5: None},
    3 : { 1: lam_1[2], 2: lam_2[2], 3: lam_3[2], 4: None, 5: None},
    4 : { 1: lam_1[3], 2: None, 3: None, 4: None, 5: None},
    5 : { 1: lam_1[4], 2: lam_2[3], 3: None, 4: None, 5: None},
    6 : { 1: None, 2: None, 3: None, 4: lam_4[1], 5: None},
    7 : { 1: None, 2: None, 3: lam_3[3], 4: None, 5: None},
    8 : { 1: None, 2: None, 3: None, 4: None, 5: lam_5[1]},
}
