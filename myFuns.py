import numpy as np

def myfun(x, k=1):
    result = []
    for each in x:
        if np.abs(each) <= k:
            result.append(1-np.abs(each/k))
        else:
            result.append(0)
    return result

def myfun_piece(x, k=1):
    result = []
    for each in x:
        if -k < each <= 0:
            result.append(myfun_piece_left(each/k))
        elif 0 < each <= k:
            result.append(myfun_piece_right(each/k))
        else:
            result.append(0)
    return result

def myfun_piece_left(x):
    return 1/2

def myfun_piece_right(x):
    return 1-x