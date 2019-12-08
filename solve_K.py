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
    mi_2 = mi[1]
    mi_3 = mi[2]
    mi_4 = mi[3]
    mi_5 = mi[4]
    mi_6 = mi[5]
    mi_7 = mi[6]
    mi_8 = mi[7]


    # System 1 - Typ IS
    print "System 1:"
    # Klasa 1
    K_1_1 = calc_K_IS(lam[1][1], mi_1)

    # Klasa 2
    K_1_2 = calc_K_IS(lam[1][2], mi_1)

    # Klasa 3
    K_1_3 = calc_K_IS(lam[1][3], mi_1)

    # Klasa 4
    K_1_4 = calc_K_IS(lam[1][4], mi_1)

    # Klasa 5
    K_1_5 = calc_K_IS(lam[1][5], mi_1)

    print [K_1_1, K_1_2, K_1_3, K_1_4, K_1_5]


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
