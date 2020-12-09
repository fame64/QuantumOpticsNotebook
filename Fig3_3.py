#FIGURE 3.3

#Make a 3D plot of the evolution of the wavefunction for a coherent state in a Harmonic potential, thus demonstrating that the shape is preserved

import numpy as np
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['font.size']=20
import matplotlib.pyplot as plt
w=1
#\hbar=1 so q and \xi are the same
i=complex(0,1)
a=0.5#|alpha|
theta=np.pi/2 #arg(alpha)
def f(q, t):
    return np.exp(q**2/2 - a**2/2 - (q-a*np.exp(-i*(w*t- theta))/np.sqrt(2))**2)/np.sqrt(np.sqrt(np.pi))
n_p_q=500
n_p_t=18
q=np.linspace(-2, 2, n_p_q)
t=np.linspace(0, 2*np.pi, n_p_t)
Q,T=np.meshgrid(q,t)
p_res=np.zeros((n_p_q, n_p_t))
for j in range(n_p_t):
    p_res[:,j]=np.abs(f(q, t[j]))**2
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=[10,8])
ax = fig.add_subplot(111, projection='3d')
aux=np.ones(n_p_q)/np.pi
for j in range(n_p_t):
    plt.plot(q, t[j]*aux, p_res[:,j], color='black', alpha=0.8)
Z=Q**2/2
ax.plot_surface(Q, T/np.pi,Z, color='red', alpha=0.3 )
ax.set_zlim(0, 1.5)
ax.set_xlabel('$q$')
ax.set_ylabel('$t/\pi$')
ax.set_zlabel(r'$|\psi_\alpha(q, t)|^2$')
ax.set_zticks([0, 1])
ax.set_xticks([-2, -1, 0, 1, 2])
ax.set_yticks([0, 1, 2])
plt.show()
