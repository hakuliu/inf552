from cvxopt import matrix, solvers
import numpy as npy
import math

class SVM:
    def __init__(self, data):
        self.data = data

    def constructQPMatrices(self):
        N = len(self.data)

        P = npy.zeros((N, N))
        for n in range(N):
            dn = self.data[n]
            for m in range(N):
                dm = self.data[m]
                yy = dn.val * dm.val
                xTx = self.kernel(dn.x, dm.x, dn.y, dm.y)
                P[n, m] = yy * xTx
        self.P = matrix(P)

        q = npy.ones(N)
        q = -1 * q
        self.q = matrix(q)

        G = npy.ones(N)
        G = -1 * G
        G = npy.diag(G)
        self.G = matrix(G)

        h = npy.zeros(N)
        self.h = matrix(h)

        A = []
        for d in self.data:
            A.append([float(d.val)])
        self.A = matrix(A, (1, N))

        b = 0.
        self.b = matrix(b)



    def kernel(cls, xn, xm, yn, ym):
        return xn * xm + yn * ym

    def solve(self):
        sol = solvers.qp(self.P, self.q, self.G, self.h, self.A, self.b)
        self.alphas = sol['x']
        print(sol['x'])

    def calcW(self):
        N = len(self.data)
        w = [0, 0]
        sx = []
        sy = []
        # get w based on sum(a * x * y)
        for i in range(N):
            a = self.alphas[i]
            if a > 0:  # only positive alphas are support vectors
                y = self.data[i].val
                ayx = [a * y * self.data[i].x,
                       a * y * self.data[i].y]
                w = [sum(aa) for aa in zip(w, ayx)]
            if a > 1: #others are sufficiently close to 0 to not count as supports
                sx.append(self.data[i].x)
                sy.append(self.data[i].y)
        self.supportx = sx
        self.supporty = sy
        self.w = w

    def calcB(self):
        N = len(self.data)
        poswTx = []
        negwTx = []
        for i in range(N):
            a = self.alphas[i]
            d = self.data[i]
            if d.val > 0:
                poswTx.append(self.w[0] * d.x + self.w[1] * d.y)
            else:
                negwTx.append(self.w[0] * d.x + self.w[1] * d.y)

        minPos = min(poswTx)
        maxNeg = max(negwTx)
        self.b = -.5 * (minPos + maxNeg)

    def getWAndb(self):
        self.calcW()
        self.calcB()
        return self.w,self.b

    def train(self):
        self.constructQPMatrices()
        self.solve()
        return self.getWAndb()

    def predict(self, x, y):
        result = self.w[0] * x + self.w[1] * y + self.b
        return self.sign(result)

    def test(self, data):
        correct = 0
        for d in data:
            prediction = self.predict(d.x, d.y)
            if prediction == d.val:
                correct = correct + 1
        return float(correct) / len(data)

    def sign(self, v):
        if v >= 0: return 1
        else: return -1

class RadialKernelSVM(SVM):
    def kernel(cls, xn, xm, yn, ym):
        GAMMA = .5
        xdiff =  xn - xm
        ydiff = yn - ym
        mag = xdiff**2 + ydiff**2
        return math.exp(-1 * GAMMA * mag)

    def predict(self, x, y):
        tosum = []
        for i in range(len(self.data)):
            d = self.data[i]
            a = self.alphas[i]
            result = a * d.val * self.kernel(d.x, x, d.y, y)
            tosum.append(result)
        return self.sign(sum(tosum))
