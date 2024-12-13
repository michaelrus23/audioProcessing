import numpy as np

def myfun_f_series(x, N=101, k=1):
    a0 = 1 / 2
    sum = []
    for each in x:
        if np.abs(each) <= k:
            temp = a0
            for n in range(1,N+1):
                temp += an(n)*np.cos(np.pi*n*each/k) + bn(n)*np.sin(np.pi*n*each/k)
            sum.append(temp)
        else:
            sum.append(0)
    return sum

def an(n):
    # return 2*(1-np.cos(np.pi*n))/(np.pi*n)/(np.pi*n)
    return (1-np.cos(np.pi*n)) / (np.pi*n) / (np.pi*n)

def bn(n):
    # return 0
    return (1 + np.cos(np.pi * n)) / (np.pi * n) / 2