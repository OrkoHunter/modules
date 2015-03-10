'''
   Developed By: Himanshu Mishra
   Email : himanshu2014iit@gmail.com

   The Guessing game

   Pick a number in your mind and help the computer guess it for you.

   First we need to set up an upper and lower limit that are viable to change.
'''

def guess():
    l_limit = 0
    u_limit = 100
    ask = (l_limit + u_limit)/2

    slot = [i for i in xrange(0,101)]

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

    return slot[0]
