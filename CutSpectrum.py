import numpy as np

def cutWindow(x):
    if 500 < np.abs(x):
        return 1
    else:
        return 0

def cutExe(f_x, x):
    for i in range(len(x)):
        f_x[i] *= cutWindow(x[i])