from cvxopt import matrix, solvers

def doExample():
    '''
    the example problem from the tutorial for the package
    :return: 
    '''
    Q = 2*matrix([ [2, .5], [.5, 1] ])
    p = matrix([1.0, 1.0])
    G = matrix([[-1.0,0.0],[0.0,-1.0]])
    h = matrix([0.0,0.0])
    A = matrix([[1.0], [1.0]])
    b = matrix(1.0)
    sol=solvers.qp(Q, p, G, h, A, b)

    print(sol['x'])

