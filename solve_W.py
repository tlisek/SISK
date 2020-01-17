def solve_W(lambda_0, Q):
        W = {
            1 : { 1: 0, 2: 0, 3: 3, 4: 4, 5: 5},
            2 : { 1: 0, 2: 0, 3: 8, 4: None, 5: None},
            3 : { 1: 0, 2: 0, 3: 3, 4: None, 5: None},
            4 : { 1: 0, 2: None, 3: None, 4: None, 5: None},
            5 : { 1: 0, 2: 0, 3: None, 4: None, 5: None},
            6 : { 1: None, 2: None, 3: None, 4: 4, 5: None},
            7 : { 1: None, 2: None, 3: 3, 4: None, 5: None},
            8 : { 1: None, 2: None, 3: None, 4: None, 5: 6},
        }
        return W
