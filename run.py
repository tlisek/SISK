import numpy as np

# System i
# Klasa r

#System 1
lam_0_1 = 1/15
A_list =[
    [0.1, 0.1, 1, -1],
    [0.6, -1, 0, 0],
    [0.3, 0.9, -1, 0.1],
    [1, 0, 0, 0]
]
b_list = [[0],[0],[0],[lam_0_2]]

#System 2
lam_0_2 = 1
A_list =[
    [-1, 0.1, 1, -1],
    [0.6, -1, 0, 0],
    [0.3, 0.9, -1, 0.1],
    [1, 0, 0, 0]
]
b_list = [[0],[0],[0],[lam_0_2]]

A = np.array(A_list)
b = np.array(b_list)
X_2 = np.linalg.inv(A).dot(b)
print X_2

#System 3
lam_0_3 = 1
A_list =[
    [0.1, 0.1, 1, -1],
    [0.6, -1, 0, 0],
    [0.3, 0.9, -1, 0.1],
    [1, 0, 0, 0]
]
b_list = [[0],[0],[0],[lam_0_2]]

A = np.array(A_list)
b = np.array(b_list)
X_3 = np.linalg.inv(A).dot(b)
print X_3


#System 4
lam_0_1 = 1/15


#System 5
lam_0_1 = 1/15
