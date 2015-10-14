#!/usr/bin/env python
from numpy import *;
from matplotlib import pyplot as plt;
import pylab;

def computeError(m, c, myfile):
	totalError = 0.0;
	for i in range(0,len(x)):
		x = myfile[i, 0]
		y = myfile[i, 1] 
		totalError += (y[i]-(m*x[i]+c))**2;
	return totalError/float(len(x));

def gradientDesc(b_current, m_current,myfile, learningRate):
	b_gradient = 0;
	m_gradient = 0;
	N = float(len(myfile))
	
	for i in range(0, len(myfile)):
		x = myfile[i, 0]
		y = myfile[i, 1]
		b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
		m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
	new_b = b_current - (learningRate * b_gradient)
	new_m = m_current - (learningRate * m_gradient)
	return [new_b, new_m]

def gradientRunner(myfile, starting_b, starting_m, learning_rate, iterations):
	b = starting_b
	m = starting_m
	for i in range(iterations):
		b, m = gradientDesc(b, m, array(myfile), learning_rate)
	return [b, m]

def run():
	myfile = loadtxt("data.txt",delimiter = ',')
	x = myfile[:,0]
	y = myfile[:,1]

	

	learning_rate = 0.0001
	initial_m = 0
	initial_b = 0
	iterations = 1000
	
	b,m = gradientRunner(myfile, initial_b, initial_m,learning_rate,iterations)
	print b,m 
	new_y = m*x+b;

	plt.scatter(x,y, marker='o', c='b')
	plt.plot(x,new_y,color = 'red')
	plt.title('Profits distribution')
	plt.xlabel('Population of City in 10,000s')
	plt.ylabel('Profit in $10,000s')
	plt.show()

if __name__ == '__main__':
	run()
