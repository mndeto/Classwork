myname = "Martin"

def findMyGrade(mark,name):
	if mark >= 80:
		print name," your are Excellent"
	elif mark >=70 and mark <80:
		print name," your are Good"
	elif mark >=60 and mark <70:
		print name," your are Poor"
	else:
		print name," your have Failed. Please enter your new mark"
		findMyGrade(mark,name)

def inputGrade(name):
	mark = input("Please enter your Marks: ")
	findMyGrade(mark,name)

def findMyname(count):
	count += 1
	rem = 3 - count
	name = raw_input("Please enter your Name: ")
	#for i in range (1,10):
	if count <3:
		if name == myname:
			count =4
			inputGrade(name)
		else:
			print "You are wrong!\nI am not ",name," You have ",rem," counts left"
			findMyname(count)
count = 0
findMyname(count)
