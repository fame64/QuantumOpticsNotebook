from mpmath import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as spsp
from scipy.optimize import curve_fit
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['font.size']=20
#a=0.5 #Modulo de alpha
a_arr=[5]
n_points=400
x_arr=np.linspace(0, 2*np.pi, n_points)
P_phi=np.zeros((n_points))
def func(x):
    aux=nsum(lambda n: exp(i*n*(t-x))*a**n/sqrt(fac(n)), [0,inf])
    P=exp(-a**2)*(fabs(aux))**2/(2*np.pi)
    return P
def Poisson(k, l, a):
    return a*np.exp(-l)*l**k/spsp.gamma(k+1)
def Gaussian(x, t, a):
    return np.sqrt(2*a**2/np.pi)*np.exp(-2*a**2*(x-t)**2)
"""for l in range(len(a_arr)):
    a=a_arr[l]
    t=np.pi/2 #Argumento de alpha
    i=complex(0,1)
    for j in range(len(x_arr)):
        P_phi[j, l]=func(x_arr[j])"""
a=a_arr[0]
t=np.pi/2 #Argumento de alpha
i=complex(0,1)
for j in range(len(x_arr)):
    P_phi[j]=func(x_arr[j])
#popt,pcov=curve_fit(Poisson, x_arr, P_phi, p0=[t, 1])
    #print(np.trapz(P_phi, x_arr))
    #print(popt, pcov)
plt.figure()
#for k in range(len(a_arr)):
    #plt.plot(x_arr, P_phi[:, k]/np.max(P_phi[:,k]), label=r'$| \alpha|=$'+str(a_arr[k]))
plt.plot(x_arr, P_phi[:], label=r'$| \alpha|=$'+str(a_arr[0]))
plt.plot(x_arr, Gaussian(x_arr, t, a), label='Gaussian fit', linestyle='--')
#plt.plot(x_arr, Poisson(x_arr, popt[0], popt[1]), linestyle='--', label='Poisson Fit')
#plt.vlines(t, -0.05, 1.05, linestyle='--', alpha=0.5, label=r'$\phi= \theta= \pi/2$')
#plt.ylabel(r"$\mathcal{P}_{\alpha}(\phi)/\mathcal{P}_{\alpha}(\phi=\theta)$")
plt.ylabel(r"$\mathcal{P}(\phi)$")
plt.xlabel("$\phi$")
#plt.ylim(-0.05, 1.05)
plt.legend(labelspacing=0)
plt.show()