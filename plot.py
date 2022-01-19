import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,1,50)
y1 = np.cos(4*np.pi*x)
plt.plot(x,y1,'r-*',lw=1)
plt.show()
