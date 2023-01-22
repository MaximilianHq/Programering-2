import sys, time, oopcafe

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./25) #change the denominators value to change type speed

cafe=oopcafe.Cafe()

cafe.order()