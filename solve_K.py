# from solve_lambda import *
import solve_lambda as Lambda_Solver
import math
from params import *
# System i
# Klasa r


def calc_K_FIFO(m_i, ro_i_r, ro_i):
    sum = 0
    for k in range(0,m_i):
        sum += 1.0 * ((m_i*ro_i)**k) / math.factorial(k)

    return m_i*ro_i_r + ro_i_r/(1-ro_i) * ((m_i*ro_i)**m_i) / ( math.factorial(m_i)*(1-ro_i) ) * 1/( sum + (((m_i*ro_i)**m_i)/(math.factorial(m_i)) ) * (1/(1-ro_i)) )

def calc_K_IS(lam_i_r,mi_i):
    return lam_i_r/mi_i


def solve_K(lambda_0, mi):

    lam = Lambda_Solver.Solve_Lambda(lambda_0)

    mi_1 = mi[0]
    mi_1_1 = mi_1[0]
    mi_1_2 = mi_1[1]
    mi_1_3 = mi_1[2]
    mi_1_4 = mi_1[3]
    mi_1_5 = mi_1[4]
    mi_2 = mi[1]
    mi_2_1 = mi_2[0]
    mi_2_2 = mi_2[1]
    mi_2_3 = mi_2[2]
    # mi_2_4 = mi_2[3]
    # mi_2_5 = mi_2[4]
    mi_3 = mi[2]
    mi_4 = mi[3]
    mi_5 = mi[4]
    mi_6 = mi[5]
    mi_7 = mi[6]
    mi_8 = mi[7]


    # System 1 - Typ IS
    print "System 1:"
    # Klasa 1
    K_1_1 = calc_K_IS(lam[1][1], mi_1_1)

    # Klasa 2
    K_1_2 = calc_K_IS(lam[1][2], mi_1_2)

    # Klasa 3
    K_1_3 = calc_K_IS(lam[1][3], mi_1_3)

    # Klasa 4
    K_1_4 = calc_K_IS(lam[1][4], mi_1_4)

    # Klasa 5
    K_1_5 = calc_K_IS(lam[1][5], mi_1_5)

    print [K_1_1, K_1_2, K_1_3, K_1_4, K_1_5]


    #System 2 - Typ IS
    print "System 2:"

    #Klasa 1
    K_2_1 = calc_K_IS(lam[2][1], mi_2_1)

    #Klasa 2
    K_2_2 = calc_K_IS(lam[2][2], mi_2_2)

    #Klasa 3
    K_2_3 = calc_K_IS(lam[2][3], mi_2_3)

    #Klasa 4
    #W systemie 2 nie ma klasy 4

    #Klasa 5
    #W systemie 2 nie ma klasy 5

    print [K_2_1, K_2_2, K_2_3]


    # System 3 - Typ FIFO
    print "System 3:"

    # Klasa 1
    ro_3_1 = lam[3][1]/(m_3*mi_3)

    # Klasa 2
    ro_3_2 = lam[3][2]/(m_3*mi_3)

    # Klasa 3
    ro_3_3 = lam[3][3]/(m_3*mi_3)

    # Klasa 4
    # W systemie 3 nie ma klasy 4

    # Klasa 5
    # W systemie 3 nie ma klasy 5

    ro_3 = (ro_3_1 + ro_3_2 + ro_3_3) / 3.0

    K_3_1 = calc_K_FIFO(m_3, ro_3_1, ro_3)
    K_3_2 = calc_K_FIFO(m_3, ro_3_2, ro_3)
    K_3_3 = calc_K_FIFO(m_3, ro_3_3, ro_3)
    print [K_3_1, K_3_2, K_3_3]


    #System 4 - Typ FIFO
    print "System 4"

    #Klasa 1
    ro_4_1 = lam[4][1]/(m_4 * mi_4)

    #Klasa 2
    #W systemie 4 nie ma klasy 2

    #Klasa 3
    #W systemie 4 nie ma klasy 3

    #Klasa 4
    #W systemie 4 nie ma klasy 4

    #Klasa 5
    #W systemie 4 nie ma klasy 5

    ro_4 = ro_4_1
    K_4_1 = calc_K_FIFO(m_4, ro_4_1, ro_4)
    print [K_4_1]


    #System 5 - Typ FIFO
    print "System 5"

    #Klasa 1
    ro_5_1 = lam[5][1]/(m_5 * mi_5)

    #Klasa 2
    ro_5_2 = lam[5][2]/(m_5 * mi_5)

    #Klasa 3
    #W systemie 5 nie ma klasy 3

    #Klasa 4
    #W systemie 5 nie ma klasy 4

    #Klasa 5
    #W systemie 5 nie ma klasy 5

    ro_5 = (ro_5_1 + ro_5_2)/2.0
    K_5_1 = calc_K_FIFO(m_5, ro_5_1, ro_5)
    K_5_2 = calc_K_FIFO(m_5, ro_5_2, ro_5)
    print [K_5_1, K_5_2]


    #System 6 - Typ FIFO
    print "System 6"

    #Klasa 1
    #W systemie 6 nie ma klasy 1

    #Klasa 2
    #W systemie 6 nie ma klasy 2

    #Klasa 3
    #W systemie 6 nie ma klasy 3

    #Klasa 4
    ro_6_4 = lam[6][4]/(m_6 * mi_6)

    #Klasa 5
    #W systemie 6 nie ma klasy 5

    ro_6 = ro_6_4
    K_6_4 = calc_K_FIFO(m_6, ro_6_4, ro_4)
    print [K_6_4]


    #System 7 - Typ FIFO
    print "System 7"

    #Klasa 1
    #W systemie 7 nie ma klasy 1

    #Klasa 2
    #W systemie 7 nie ma klasy 2

    #Klasa 3
    ro_7_3 = lam[7][3]/(m_7 * mi_7)

    #Klasa 4
    #W systemie 7 nie ma klasy 4

    #Klasa 5
    #W systemie 7 nie ma klasy 5

    ro_7 = ro_7_3
    K_7_3 = calc_K_FIFO(m_7, ro_7_3, ro_7)
    print [K_7_3]


    #System 8 - Typ FIFO
    print "System 8"

    #Klasa 1
    #W systemie 8 nie ma klasy 1

    #Klasa 2
    #W systemie 8 nie ma klasy 2

    #Klasa 3
    #W systemie 8 nie ma klasy 3

    #Klasa 4
    #W systemie 8 nie ma klasy 4

    #Klasa 5
    ro_8_5 = lam[8][5]/(m_8 * mi_8)

    ro_8 = ro_8_5
    K_8_5 = calc_K_FIFO(m_8, ro_8_5, ro_8)
    print [K_8_5]
    #test

    # K[system][klasa]
    K = {
        1 : { 1: K_1_1, 2: K_1_2, 3: K_1_3, 4: K_1_4, 5: K_1_5},
        2 : { 1: K_2_1, 2: K_2_2, 3: K_2_3, 4: None, 5: None},
        3 : { 1: K_3_1, 2: K_3_2, 3: K_3_3, 4: None, 5: None},
        4 : { 1: K_4_1, 2: None, 3: None, 4: None, 5: None},
        5 : { 1: K_5_1, 2: K_5_2, 3: None, 4: None, 5: None},
        6 : { 1: None, 2: None, 3: None, 4: K_6_4, 5: None},
        7 : { 1: None, 2: None, 3: K_7_3, 4: None, 5: None},
        8 : { 1: None, 2: None, 3: None, 4: None, 5: K_8_5},
    }
    return K
