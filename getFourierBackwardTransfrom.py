import numpy as np

class FourierTransformBackwardSpline:

    def approx(self, t):
        np.seterr(divide='ignore')
        sum = 0 + 0*1j
        hf = self.f_val[2] - self.f_val[1]
        pi2 = np.pi*np.pi
        for n in range(len(self.f_val)):
            term = self.G_val[n]*(1 - np.cos(2*np.pi*hf*t))/(2*pi2*hf*t*t)*np.exp(-1j*2*np.pi*t*self.f_val[n])
            sum += term

        return 2*np.real(sum)

    def __init__(self, fun, x):
        self.f_val = np.array(x)
        self.G_val = np.array(fun)

    def getFunValue(self):
        return lambda x : self.approx(x)