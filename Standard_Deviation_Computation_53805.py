
#Author: Martin N. Ndeto, 053805, MSc. IT

import math
items=[]	#initialize the list
noOfitems=5 	#The expected number of values
def findMean(items): #computes the Mean
	mean=sum(items)/len(items)
	findDeviation(mean,items) #Calls and Parses the mean and the list to findDeviation()

def findDeviation(mean,items):
	nums=len(items) #counts items in the list
	n=nums-1	#Gets the Numerator
	d=0		#Initializes the sum of squared Differences
	for i in items:	#Loops through the items
		a=i-mean	#Computes the difference between the mean and each value
		sq=a*a		#Computes the square of the difference
		d += sq		#Computes the sum of squared differences
		
	deviation=d/n		#Divides the sum of squared differences by the Numerator ==>deviation
	findSD(deviation)	#Calls and Parses deviation to findSD()

def findSD(deviation):
	print math.sqrt(deviation)	#Computes and Displays the square root of the deviation==> Standard Deviation

def getItems(noOfitems,items):	
	noOfitems -= 1					#Decrements the expected number of values
	itms = input("Please enter a (another) Value ")	#Captures user values
	items.append(itms)				#Adds user values to the list
	if noOfitems >0:
		getItems(noOfitems,items)	#Calls itself for the user to enter a nother value
	else:
		findMean(items)			#Calls and parses the list to findMean()

getItems(noOfitems,items)			#Call and parses the expected number of items and the current list to getItems()
						#This is the first Function to be executed
