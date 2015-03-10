def isPrime(no):
	if no==2:
		return True
	if no%2==0:
		return False
	else:
		for x in xrange(3,int(no**0.5)+2,2):
			if no%x==0:
				return False
			elif x==int(no**0.5) or x==int(no**0.5)+1:
				return True
			pass

def lfactor(no):
	divisor=1.0

	while(True):
		divisor+=1
		quotient=no/divisor
		if int(quotient)==quotient:
			if isPrime(quotient):
		 		return int(quotient)
		 		break
