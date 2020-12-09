#FIGURE 2.1

#Plot the occupation probability for different values of <n>

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['font.size']=23
#matplotlib.rcParams['text.usetex'] = True
n= np.arange(0, 11, 1)
N=3
f=N**n/((1+N)**(n+1))
plt.figure()
plt.bar(n, f, color='red', width=0.9 , label=r"$\mathcal{P}_n \; \mathrm{for} \; \langle n \rangle =$"+ str(N))
plt.xlabel("$n$")
plt.ylabel("$\mathcal{P}_n$")
plt.legend()
#plt.savefig("QOQI_PnPlot1.png")
plt.show()
