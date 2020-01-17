def solve_T(lambda_0, K):
    print "---solve_T---"
    print lambda_0[0]


    T={}
    for (sys,i) in zip(K.values(), range(8)):
        T_sys = {}
        for (K_value, j) in zip(sys.values(), range(6)):
            if K_value != None: T_sys[j+1]=K_value/lambda_0[j]
            else: T_sys[j+1]=None
        T[i+1] = T_sys

    return T
