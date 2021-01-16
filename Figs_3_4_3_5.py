import numpy as np
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['font.size']=18
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import laguerre

#beta=x0+iy0
#x0=1
#y0=1
#Number state
n=4
def W(x, y):
    #Coherent state
    #return 2/np.pi* np.exp(-2*(x-x0)**2-2*(y-y0)**2)
    #Number state
    L = laguerre(n)
    return 2/np.pi* (-1)**n * L(4*(x**2 + y**2))*np.exp(-2*(x**2+y**2))
#q=np.linspace(x0-1.5, x0+1.5, 1000)
#p=np.linspace(y0-1.5, y0+1.5, 1000)
limit=2
n_points=5000
q=np.linspace(-limit,limit, n_points)
p=np.linspace(-limit, limit, n_points)
Q,P=np.meshgrid(q, p)
fig = plt.figure(figsize=[10,8])
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(Q,P,W(Q,P), color='cyan', shade=True)
ax.set_xlabel("$x$")
ax.set_ylabel("$p$")
ax.set_zlabel(r"$W_n(x,p)$")
ax.set_xticks([-2, -1, 0, 1, 2])
ax.set_yticks([-2, -1, 0, 1, 2])
plt.show()
