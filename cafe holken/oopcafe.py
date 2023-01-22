import sys, time, random

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./25) #change the denominators value to change type speed
  

class Coffee:
    def __init__(self):
        
        self.price_small=10
        self.price_regular=20
        self.price_large=30
        self.price_topping=5
        
        self.gamble=random.randint(10,60)
        
        self.coffee="none"
        self.temperature="hot"
        self.topping="none"
        
    def casino(self):
        slowprint("Slot machine - Press ENTER to gamble...")
        val=input()
        
        if val=="":
            slowprint("\nSystem - You gambled and won!...\nYour current balance is: "+ \
                str(self.gamble)+"kr")
        else:
            print("die")
            
    def choose_item(self):
        while True:
            slowprint("\nsmall coffee: "+ str(self.price_small)+"kr"\
                "\nregular coffee: "+ str(self.price_regular)+"kr"\
                "\nlarge coffee:" + str(self.price_large)+"kr"\
                "\n\nWhat would you like to order?")
            choice=input()
            self.coffee=choice
            
            if choice=="small coffee" and self.gamble>=self.price_small:
                self.gamble-=self.price_small
                break
            elif choice=="regular coffee" and self.gamble>=self.price_regular:
                self.gamble-=self.price_regular
                break
            elif choice=="large coffee" and self.gamble>=self.price_large:
                self.gamble-=self.price_large
                break
            else: 
                slowprint("\nSystem - You do not have sufficient funds for this item...")
            
    def choose_temperature(self):
        slowprint("\nCashier - What temperature do you want your coffee?..."\
            "\ncold\nmedium\nhot\n")
        self.temperature=input()
            
    def choose_topping(self):
         if self.gamble>=5:
            slowprint("\nCashier - Whould you like to add a topping to your coffee?"\
            "\nchoco\nfoam\nno\n")
            self.topping=input()
            if self.topping!="no" or self.topping!="":
                self.gamble-=self.price_topping
            else:
                self.topping="no"
  
    def OopCafe(self):
        slowprint("\nNarrator - You walk down the road after winning the grand price of "+\
            str(self.gamble)+"\nkr, and suddenly there is a cafe standing before you."+\
            "\nYou decide to enter the cafe and you walk up the the cashier..."\
            "\n\nCashier - Welcome to our café!...")
        
        Coffee.choose_item(self)        
        Coffee.choose_temperature(self)
        Coffee.choose_topping(self)
            
        slowprint("\nSystem - Crafting...   ...   ...   ...")
        slowprint("Cashier - Here is your "+ str(self.temperature)+" "+str(self.coffee)+\
            " with "+str(self.topping)+" topping.\nChange: "+str(self.gamble)+"kr")