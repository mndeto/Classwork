try:
	fh=open("bar.py","r+")
	fh.write("Am testing exeption handling")
except IOError:
	print "You are joking, I can\'t read this file!"
else:
	print "Wow! I have manged to write!"
