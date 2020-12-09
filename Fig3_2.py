#FIGURE 3.2

#Plot the probability of the number of photons in a coherent state for different \bar(n)

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import scipy.special as sp
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['font.size']=23
#matplotlib.rcParams['text.usetex'] = True
n= np.arange(0, 21, 1)
N=np.asarray([3,6,12])
#f=N**n/((1+N)**(n+1))
f=np.zeros((len(n), len(N)))
plt.figure()
c_arr=['blue', 'red', 'green']
for j in range(len(N)):
    f[:, j]=np.exp(-N[j])*N[j]**n/(sp.factorial(n))
    plt.bar(n, np.abs(f)[:,j], width=0.9, color=c_arr[j], alpha=0.3, label=r"$\mathcal{P}_n \; \mathrm{for} \; \bar{n}=$"+ str(N[j]))
    plt.scatter(n, np.abs(f)[:,j], color=c_arr[j])
plt.xlabel("$n$")
plt.ylabel("$\mathcal{P}_n$")
plt.legend(labelspacing=0)
plt.savefig("QOQI_PnPlot1.png")
plt.ylim(0,)
plt.show()
