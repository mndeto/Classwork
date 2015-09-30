import matplotlib.pyplot as plt
import numpy as np
a=np.linspace(0,10,100)
b=np.exp(-a**2)
plt.xlabel("the value of a")
plt.ylabel("the value of b")
plt.plot(a,b,color="green",linewidth=1.0, linestyle="-")
plt.show()
