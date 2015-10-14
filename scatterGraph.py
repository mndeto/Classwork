from numpy import *;
from matplotlib import pyplot as plt;
import pylab; 
def scattering():
        myfile = loadtxt("data.txt",delimiter = ',')
        x = myfile[:,0]
        y = myfile[:,1]
        plt.scatter(x,y)
scattering()
