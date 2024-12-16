import numpy as np
import matplotlib.pyplot as plt
from Fourier_series import myfun_f_series
from myFuns import myfun, myfun_piece

x = np.linspace(-2,2,1001)
plt.figure()
# y = myfun(x)
# yf = myfun_f_series(x, N=4)
#
# plt.rcParams['font.family'] = 'Comic Sans MS'
# hfont = {'fontname' : 'Comic Sans MS'}
# plt.plot(x, y, label="Прямое вычисление")
# plt.plot(x, yf, '--', label="Слагаемых Фурье N = 4")
# plt.xlabel('x', size=12, **hfont)
# plt.xticks(size=12, **hfont)
# plt.ylabel('u(x)', size=12, **hfont)
# plt.yticks(size=12, **hfont)
# plt.legend()
# plt.show()

y = myfun_piece(x)
yf = myfun_f_series(x, N=16)

plt.rcParams['font.family'] = 'Comic Sans MS'
hfont = {'fontname' : 'Comic Sans MS'}
plt.plot(x, y, '.', label="Прямое вычисление")
plt.plot(x, yf, '-.', label="Слагаемых Фурье N = 4")
plt.xlabel('x', size=24, **hfont)
plt.xticks(size=24, **hfont)
plt.ylabel('u(x)', size=24, **hfont)
plt.yticks(size=24, **hfont)
plt.legend()
plt.show()



