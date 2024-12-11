import numpy as np

class FourierTransformSpline:

    def approx(self, f):
        np.seterr(divide='ignore')
        sum = 0 + 0*1j
        ht = self.t_val[2] - self.t_val[1]
        arg = 2*np.pi*f
        for n in range(len(self.t_val)):
            term = self.g_t[n]*2*(1 - np.cos(arg*ht))/(arg*arg*ht)*np.exp(1j*arg*self.t_val[n])
            sum += term

        return sum

    def __init__(self, fun, x):
        self.t_val = np.array(x)
        self.g_t = np.array(fun)

    def getFunValue(self):
        return lambda x : self.approx(x)