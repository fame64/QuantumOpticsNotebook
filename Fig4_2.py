from mpmath import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as spsp
from scipy.optimize import curve_fit
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['font.size']=20
n_points= 1000
l=10 #lambda
t_f=4
t_arr=np.linspace(0, t_f, n_points )
nb=5 #bar(n)
def W(t):
    aux=nsum(lambda n:  nb**n/fac(n)*cos(2* sqrt(n+1)*l*t), [0, inf])
    return exp(-nb)* aux
W_arr=np.zeros(n_points)
for i in range(n_points):
    W_arr[i]=W(t_arr[i])
#print(W_arr)
t_R=np.pi/(l*(np.sqrt(nb+1)-np.sqrt(nb))) #k=1
t_R_ap=2* np.pi/(l)*np.sqrt(nb)
plt.figure()
plt.plot(l*t_arr, W_arr, color='red')
plt.xlabel("$\lambda t$")
plt.ylabel("$W(t)$")
plt.vlines(l* t_R_ap, -1, 1, linestyle='--', color='green', label='Approximation')
plt.vlines(l* t_R, -1, 1, linestyle='dotted', color='blue', label='Exact')
plt.vlines(2* l* t_R_ap, -1, 1, linestyle='--', color='green')
plt.vlines(2* l* t_R, -1, 1, linestyle='dotted', color='blue')
plt.xlim(0, l* t_f)
plt.ylim(-1, 1)
plt.legend(labelspacing=0)
plt.text(30, -1.4, r"$\bar{n}= $"+str(nb))
plt.show()
