import numpy as np
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['font.size']=18
import matplotlib.pyplot as plt
V=1  #V/hbar
D=1 #Delta
R=np.sqrt(V**2+ D**2)
n_p=1000
t=np.linspace(0, 2* np.pi/R*4, n_p)
i=complex(0,1)
C_e=-i*V*np.sin(R*t/2)/R
C_g=(np.cos(R*t/2)+ i* D*np.sin(R*t/2)/R)
P_e=np.abs(C_e)**2
P_g=np.abs(C_g)**2
plt.figure()
plt.plot(t*R/np.pi/2, P_e, color='red', label="$P_e$")
plt.plot(t*R/np.pi/2, P_g, color='blue', label="$P_g$")
plt.plot(t*R/np.pi/2, P_e+P_g, linestyle='--', color='black', label="$P_e+ P_g$")
plt.ylabel("$P(t)$")
plt.xlabel("$\Omega_R t/2\pi$")
plt.legend(labelspacing=0, loc='upper right')
plt.text(3, -0.25,"$\hbar\Delta/\mathcal{V}=$"+str(D/V))
plt.show()
