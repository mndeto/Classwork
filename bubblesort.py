def bubbleSort(items):
    for tester in range(len(items)-1,0,-1):
        for i in range(tester ):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
		print "Now sorting",items[i]
		print "current List = ",items
		print "\n"

items= [53,456,90,107,16,3,60,15,80]
bubbleSort(items)
print(items)
