import solve_lambda as Lambda_Solver

def solve_W(lambda_0, Q):

    lam = Lambda_Solver.Solve_Lambda(lambda_0)

    print "---solve_W---"


    W={}
    for (sys,i) in zip(Q.values(), range(8)):
        W_sys = {}
        for (Q_value, j) in zip(sys.values(), range(6)):
            if Q_value != None: W_sys[j+1]=Q_value/lam[i+1][j+1]
            else: W_sys[j+1]=None
        W[i+1] = W_sys

    return W
