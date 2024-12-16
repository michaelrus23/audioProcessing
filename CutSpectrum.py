import numpy as np

def cutWindow(x):
    if np.abs(x) > 650:
        return 0
    else:
        return 1

def cutExe(f_x, x):
    for i in range(len(x)):
        f_x[i] *= cutWindow(x[i])