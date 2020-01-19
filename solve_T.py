import solve_lambda as Lambda_Solver

def solve_T(lambda_0, K):

    lam = Lambda_Solver.Solve_Lambda(lambda_0)

    #print lam

    print "---solve_T---"

    T={}
    for (sys,i) in zip(K.values(), range(8)):
        T_sys = {}
        for (K_value, j) in zip(sys.values(), range(6)):

            #print [i, j]

            if K_value != None: T_sys[j+1]=K_value/lam[i+1][j+1]
            else: T_sys[j+1]=None
        T[i+1] = T_sys

    return T
