import solve_lambda as Lambda_Solver
import math
from params import *

def calc_Pi0_FIFO(m_i, ro_i_r):
    sum = 0
    for k in range(0,m_i):
        sum += 1.0 * ((ro_i_r)**k) / math.factorial(k)

    #print [sum, m_i, ro_i_r]

    return 1.0 / ( sum + ( (ro_i_r**m_i)/( math.factorial(m_i-1) * (m_i - ro_i_r ) ) ) )


def calc_Q_FIFO(m_i, ro_i_r, pi0_i_r):
    W = (pi0_i_r * ro_i_r**(m_i+1)) / ((m_i - ro_i_r)**2 * math.factorial(m_i-1));
    return max(W, 0)


def solve_Q(lambda_0, mi):

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
    Q_1_1 = 0

    # Klasa 2
    Q_1_2 = 0

    # Klasa 3
    Q_1_3 = 0

    # Klasa 4
    Q_1_4 = 0

    # Klasa 5
    Q_1_5 = 0

    print [Q_1_1, Q_1_2, Q_1_3, Q_1_4, Q_1_5]


    #System 2 - Typ IS
    print "System 2:"

    #Klasa 1
    Q_2_1 = 0

    #Klasa 2
    Q_2_2 = 0

    #Klasa 3
    Q_2_3 = 0

    #Klasa 4
    #W systemie 2 nie ma klasy 4

    #Klasa 5
    #W systemie 2 nie ma klasy 5

    print [Q_2_1, Q_2_2, Q_2_3]


    # System 3 - Typ FIFO
    print "System 3:"

    # Klasa 1
    ro_3_1 = lam[3][1]/(m_3*mi_3)
    pi0_3_1 = calc_Pi0_FIFO(m_3, ro_3_1)

    # Klasa 2
    ro_3_2 = lam[3][2]/(m_3*mi_3)
    pi0_3_2 = calc_Pi0_FIFO(m_3, ro_3_2)

    # Klasa 3
    ro_3_3 = lam[3][3]/(m_3*mi_3)
    pi0_3_3 = calc_Pi0_FIFO(m_3, ro_3_3)

    # Klasa 4
    # W systemie 3 nie ma klasy 4

    # Klasa 5
    # W systemie 3 nie ma klasy 5

    #ro_3 = (ro_3_1 + ro_3_2 + ro_3_3) / 3.0

    Q_3_1 = calc_Q_FIFO(m_3, ro_3_1, pi0_3_1)
    Q_3_2 = calc_Q_FIFO(m_3, ro_3_2, pi0_3_2)
    Q_3_3 = calc_Q_FIFO(m_3, ro_3_3, pi0_3_3)
    print [Q_3_1, Q_3_2, Q_3_3]


    #System 4 - Typ FIFO
    print "System 4"

    #Klasa 1
    ro_4_1 = lam[4][1]/(m_4 * mi_4)
    pi0_4_1 = calc_Pi0_FIFO(m_4, ro_4_1)

    #Klasa 2
    #W systemie 4 nie ma klasy 2

    #Klasa 3
    #W systemie 4 nie ma klasy 3

    #Klasa 4
    #W systemie 4 nie ma klasy 4

    #Klasa 5
    #W systemie 4 nie ma klasy 5

    #ro_4 = ro_4_1

    Q_4_1 = calc_Q_FIFO(m_4, ro_4_1, pi0_4_1)
    print [Q_4_1]


    #System 5 - Typ FIFO
    print "System 5"

    #Klasa 1
    ro_5_1 = lam[5][1]/(m_5 * mi_5)
    pi0_5_1 = calc_Pi0_FIFO(m_5, ro_5_1)

    #Klasa 2
    ro_5_2 = lam[5][2]/(m_5 * mi_5)
    pi0_5_2 = calc_Pi0_FIFO(m_5, ro_5_2)

    #Klasa 3
    #W systemie 5 nie ma klasy 3

    #Klasa 4
    #W systemie 5 nie ma klasy 4

    #Klasa 5
    #W systemie 5 nie ma klasy 5

    #ro_5 = (ro_5_1 + ro_5_2)/2.0

    Q_5_1 = calc_Q_FIFO(m_5, ro_5_1, pi0_5_1)
    Q_5_2 = calc_Q_FIFO(m_5, ro_5_2, pi0_5_2)
    print [Q_5_1, Q_5_2]


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
    pi0_6_4 = calc_Pi0_FIFO(m_6, ro_6_4)

    #Klasa 5
    #W systemie 6 nie ma klasy 5

    #ro_6 = ro_6_4

    Q_6_4 = calc_Q_FIFO(m_6, ro_6_4, pi0_6_4)
    print [Q_6_4]


    #System 7 - Typ FIFO
    print "System 7"

    #Klasa 1
    #W systemie 7 nie ma klasy 1

    #Klasa 2
    #W systemie 7 nie ma klasy 2

    #Klasa 3
    ro_7_3 = lam[7][3]/(m_7 * mi_7)
    pi0_7_3 = calc_Pi0_FIFO(m_7, ro_7_3)

    #Klasa 4
    #W systemie 7 nie ma klasy 4

    #Klasa 5
    #W systemie 7 nie ma klasy 5

    #ro_7 = ro_7_3
    Q_7_3 = calc_Q_FIFO(m_7, ro_7_3, pi0_7_3)
    print [Q_7_3]


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
    pi0_8_5 = calc_Pi0_FIFO(m_8, ro_8_5)

    #ro_8 = ro_8_5
    Q_8_5 = calc_Q_FIFO(m_8, ro_8_5, pi0_8_5)
    print [Q_8_5]
    #test

    # K[system][klasa]
    Q = {
        1 : { 1: Q_1_1, 2: Q_1_2, 3: Q_1_3, 4: Q_1_4, 5: Q_1_5},
        2 : { 1: Q_2_1, 2: Q_2_2, 3: Q_2_3, 4: None, 5: None},
        3 : { 1: Q_3_1, 2: Q_3_2, 3: Q_3_3, 4: None, 5: None},
        4 : { 1: Q_4_1, 2: None, 3: None, 4: None, 5: None},
        5 : { 1: Q_5_1, 2: Q_5_2, 3: None, 4: None, 5: None},
        6 : { 1: None, 2: None, 3: None, 4: Q_6_4, 5: None},
        7 : { 1: None, 2: None, 3: Q_7_3, 4: None, 5: None},
        8 : { 1: None, 2: None, 3: None, 4: None, 5: Q_8_5},
    }
    return Q
