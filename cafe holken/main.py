import sys, time, oopcafe

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./25) #change the denominators value to change type speed

cafe=oopcafe.Coffee()

cafe.casino()

while True:
    cafe.OopCafe()

    if cafe.gamble>=cafe.price_small:
        slowprint("Cashier - You have money left, would you like to order something else?\n")
        val=input()
        if val=="yes" or val=="Yes" or val=="y":
            slowprint("System - Crurrent balance: "+str(cafe.gamble)+"kr")
            continue
        else:
            break
    else:
        break