
import matplotlib.pyplot as plt
import math
items=[]
noOfitems=5

def Chora(x,y):
	plt.xlabel("x")
	plt.ylabel("variance")
	plt.plot(x,y,color="green",linewidth=1.0, linestyle="-")
	plt.show()

def findMean(items):
	mean=sum(items)/len(items)
	findDeviation(mean,items)

def findDeviation(mean,items):
	nums=len(items)
	n=nums-1
	d=0
	x=[]
	y=[]
	for i in items:
		x.append(i)
		a=i-mean
		sq=a*a
		y.append(sq)
		d += sq
		
	deviation=d/n	
	findSD(deviation,x,y)

def findSD(deviation,x,y):
	print math.sqrt(deviation)
	Chora(x,y)

def getItems(noOfitems,items):
	noOfitems -= 1
	rem = 3 - noOfitems
	itms = input("Please enter a (another) Value ")
	items.append(itms)
	if noOfitems >0:
		getItems(noOfitems,items)
	else:
		findMean(items)

getItems(noOfitems,items)

