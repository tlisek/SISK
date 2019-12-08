import numpy as np

# System i
# Klasa r

#System 1
lam_0_1 = 1
A_list =[
    [-1, 0, 0, 0, 0],
    [0.6, -1, 0, 0, 0],
    [0.3, 0.9, -1, 0.05, 0.05],
    [0.05, 0.05, 0.5, -1, 0],
    [0.05, 0.05, 0.5, 0, -1],
]
b_list = [[lam_0_1], [0],[0],[0],[0]]
A = np.array(A_list)
b = np.array(b_list)
lam_1 = np.linalg.inv(A).dot(b)
print "\n"
print "System 1"
print "Lambda"
print lam_1

#System 2
lam_0_2 = 1
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
print "\n"
print "System 2"
print "Lambda"
print lam_2

#System 3
lam_0_3 = 1
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
print "\n"
print "System 3"
print "Lambda"
print lam_3


#System 4
lam_0_4 = 1
A_list = [
    [1, -1],
    [1, 0]
]
b_list = [[0], [lam_0_4]]

A = np.array(A_list)
b = np.array(b_list)
lam_4 = np.linalg.inv(A).dot(b)
print "\n"
print "System 4"
print "Lambda"
print lam_4

#System 5
lam_0_5 = 1
A_list = [
    [1, -1],
    [1, 0]
]
b_list = [[0], [lam_0_5]]

A = np.array(A_list)
b = np.array(b_list)
lam_5 = np.linalg.inv(A).dot(b)
print "\n"
print "System 5"
print "Lambda"
print lam_5
