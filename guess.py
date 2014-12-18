print "Imagine a number from 0 to 100."
print "Done? Okay now help me find out."

l_limit = 0
u_limit = 100
ask = (l_limit + u_limit)/2
slot = [] #Set of possible answers

for x in xrange(0,101):
	slot.append(x)
	pass

while(1):
	print ("Is your number less than or equal to %d ? (y/n) : ") % ask
	Input = raw_input()

	trim = slot.index(ask+1)
	if Input == 'y' or Input == 'Y':
		slot = slot[:(trim)]
		pass
	elif Input=='n' or Input == 'N':
		slot = slot[(trim):]
		pass


	l_limit = slot[0]
	u_limit = slot[-1]
	ask = (l_limit + u_limit)/2

	if len(slot)==1:
		break

print "Your number is %d" % slot[0]

