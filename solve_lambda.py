import numpy as np

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

def Solve_Lambda(lambda_0):

    print "Lambda 0"
    print lambda_0

    lam_0_1 = lambda_0[0]
    lam_0_2 = lambda_0[1]
    lam_0_3 = lambda_0[2]
    lam_0_4 = lambda_0[3]
    lam_0_5 = lambda_0[4]

    #Klasa 1
    # A_list =[
    #     [-1, 0, 0, 0, 0],
    #     [0.6, -1, 0, 0, 0],
    #     [0.3, 0.9, -1, 0.05, 0.05],
    #     [0.05, 0.05, 0.5, -1, 0],
    #     [0.05, 0.05, 0.5, 0, -1],
    # ]
    A_list = read_A_matrix('input_data/A1.txt')
    b_list = [[-lam_0_1], [0],[0],[0],[0]]
    A = np.array(A_list)
    b = np.array(b_list)
    lam_1 = np.linalg.inv(A).dot(b)
    lam_1 = [el[0] for el in lam_1]

    # print "Klasa 1"
    # print A
    # print "Lambda"
    # print lam_1

    #Klasa 2
    # A_list =[
    #     [0.1, 0.1, 1, -1],
    #     [0.6, -1, 0, 0],
    #     [0.3, 0.9, -1, 0.1],
    #     [1, 0, 0, 0]
    # ]
    A_list = read_A_matrix('input_data/A2.txt')
    b_list = [[-lam_0_2],[0],[0],[0]]

    A = np.array(A_list)
    b = np.array(b_list)
    lam_2 = np.linalg.inv(A).dot(b)
    lam_2 = [el[0] for el in lam_2]

    # print "\n"
    # print "Klasa 2"
    # print "Lambda"
    # print lam_2

    #Klasa 3
    # A_list =[
    #     [0.1, 0.1, 1, -1],
    #     [0.6, -1, 0, 0],
    #     [0.3, 0.9, -1, 0.1],
    #     [1, 0, 0, 0]
    # ]
    A_list = read_A_matrix('input_data/A3.txt')
    b_list = [[-lam_0_3],[0],[0],[0]]

    A = np.array(A_list)
    b = np.array(b_list)
    lam_3 = np.linalg.inv(A).dot(b)
    lam_3 = [el[0] for el in lam_3]

    # print "\n"
    # print "Klasa 3"
    # print "Lambda"
    # print lam_3


    #Klasa 4
    # A_list = [
    #     [1, -1],
    #     [1, 0]
    # ]
    A_list = read_A_matrix('input_data/A4.txt')
    b_list = [[-lam_0_4],[0]]

    A = np.array(A_list)
    b = np.array(b_list)
    lam_4 = np.linalg.inv(A).dot(b)
    lam_4 = [el[0] for el in lam_4]

    # print "\n"
    # print "Klasa 4"
    # print "Lambda"
    # print lam_4

    #Klasa 5
    # A_list = [
    #     [1, -1],
    #     [1, 0]
    # ]
    A_list = read_A_matrix('input_data/A5.txt')
    b_list = [[-lam_0_5],[0]]

    A = np.array(A_list)
    b = np.array(b_list)
    lam_5 = np.linalg.inv(A).dot(b)
    lam_5 = [el[0] for el in lam_5]

    # print "\n"
    # print "Klasa 5"
    # print "Lambda"
    # print lam_5

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

    print "Lambda"

    for key in lam:
        print lam[key]

    return lam
