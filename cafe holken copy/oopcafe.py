import sys, time, copy

#slowprint, print text(s) character for character
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
        #defines typing speed
		time.sleep(1./30) #change the denominators value to change type speed

#slowprint with different typing speed
def slowprint2(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
        #defines typing speed
		time.sleep(1./5) #change the denominators value to change type speed
  
class Product:
    #give every produkt a name and a price
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def add_item():
        pass
    
class Menu:
    def __init__(self):
        self.products = list()
        
        #add class from Coffee
        coffee = Coffee("coffee", 10)
        #add type to Coffee
        coffee.add_size("small", 10)
        coffee.add_size("medium", 20)
        coffee.add_size("large", 30)
        self.products.append(coffee)
        
        #add class from Coffee
        espresso = Coffee("espresso", 15)
        #add type to Coffee
        espresso.add_size("small", 15)
        espresso.add_size("medium", 25)
        self.products.append(espresso)
        
        #add class from Pie
        pie = Pie("pie", 40)
        #add type to Pie
        pie.add_type("cherry", 40)
        pie.add_type("apple", 40)
        pie.add_type("raspberry", 40)
        self.products.append(pie)

    def display_menu(self):
        #print the name and price of every product
        for item in self.products:
            slowprint(f"{item.name} : {item.price}kr")
        
    def verify_product(self, choice):
        #verify that input matches avalible products and return item index
        for index, item in enumerate(self.products):
            if item.name==choice:
                return index
        else:
            return "null"

    def get_item(self, index):
        #return item properties from products
        return self.products[index]

class Coffee (Product):
    def __init__(self, name, price):
        #inherit constructors och functions from Product
        super().__init__(name, price)
        self.size = list()
    
    def add_size(self, name, price):
        self.size.append((name, price))

    def add_item(self):
        while True:
            slowprint(f"\nWhat size would you like your {self.name}?\n")
            for size in self.size:
                #display items inside of list 0=name 1=price
                slowprint(f"{size[0]} : {size[1]}kr")
            val=input()
            for size in self.size:
                #if matches name of product
                if val==size[0]:
                    #change the main products name and class (inherited from Product)
                    self.price=size[1]
                    self.name=f"{size[0]} {self.name}"
                    return
            else:
                slowprint("\nThis is not a valid option!")
    
class Pie (Product):
    def __init__(self, name, price):
        #inherit constructors och functions from Product
        super().__init__(name, price)
        self.type = list()
        
    def add_type(self, name, price):
        self.type.append((name, price))
        
    def add_item(self):
        while True:
            slowprint("\nWhat type of pie would you like?\n")
            for type in self.type:
                #display items inside of list 0=name 1=price
                slowprint(f"{type[0]} : {type[1]}kr")
            val=input()
            for type in self.type:
                #if matches name of product
                if val==type[0]:
                    #change the main products name and class (inherited from Product)
                    self.price=type[1]
                    self.name=f"{type[0]} pie"
                    return
            else:
                slowprint("\nThis is not a valid option!")
            
class Customer:
    def __init__(self):
        self.basket=list()

    def add_item(self, item):
        self.basket.append(item)
    
class Cafe():
    def __init__(self):
        self.menu=Menu()
        self.current_customer=Customer()
        self.banner="•───────•°•❀ •°•───────•"

    def draw_banner(self):
        print(f"\n{self.banner}\n")

    def intro(self):
        slowprint("""You awaken from a deep slumber one fine autumn morning...
As you rise from the bedsheets you notice that you throat is soar...
With parched lips you go straight outside looking for a nice place to 
eat breakfast...\nAs you walk along the busy street lost in you own thoughts,
you find yourself distracted by a display inside of a cafe that you have never 
noticed before...""")
        slowprint2("You step inside...  ")

    def init_menu(self):
        #creates a new customer each time
        self.current_customer=Customer()
        self.order()
        while True:
            self.draw_banner()
            slowprint("❀ Order\n❀ Basket\n❀ Checkout")
            self.draw_banner()
            val=input()
            if val=="order":
                self.order()
            elif val=="basket":
                self.display_basket()
            elif val=="checkout":
                self.checkout()
                return
            else:
                slowprint("\nThis is not a valid option!")
            
    def order(self):
        self.draw_banner()
        while True:
            slowprint("What would you like to order?\n")
            self.menu.display_menu()
            choice = input()
            #verify choice and return item index
            choice_index = self.menu.verify_product(choice)
            if choice_index == "null":
                slowprint("\nThere is no such item...\n")
            else:
                break

        #create a copy of an item recieved from function
        item=copy.copy(self.menu.get_item(choice_index))
        #function add_item connected to the specific class
        item.add_item()
        slowprint(f"\nSuccesfully added {item.name} to basket!")
        self.current_customer.add_item(item)
        
    def calc_total(self):
        total=0
        #calculate total price
        for item in self.current_customer.basket:
            total+=item.price
        return total

    def display_basket(self):
        self.draw_banner()
        total=self.calc_total()
        #print item name and price from basket
        for item in self.current_customer.basket:
            slowprint(f"{item.name} : {item.price}kr")
        slowprint(f"\nYour total is: {total}kr")
            

    def checkout(self):
        ending=Ending()
        total=self.calc_total()
        slowprint(f"\nThank you for dining at our café! Your total will be {total}kr.\n\nCard\nCash\nRob")
        while True:
            val=input()
            if val=="card":
                ending.ending_1()
                return
            elif val=="cash":
                ending.ending_2()
                return
            elif val=="rob":
                ending.ending_3()
                return
            else:
                slowprint("\nThis is not a valid option!")

class Ending:
    def __init__(self):
        self.name="stranger"

    def ending_1(self):
        slowprint("\nplease enter card credentials: XXXX-XXXX-XXXX-XXXX mm/åå CVC")
        credentials=input()
        #write to text file
        with open('card.txt', 'a') as f:
            f.write(credentials)
            
    def ending_2(self):
        slowprint2("*\ngive money*")
        input()

    def ending_3(self):
        slowprint2("\nAttempting robbery...")
        slowprint("""
      ----.
     "   _}
     "@   >
     |\   7
     / `-- _         ,-------,****
  ~    >o<  \---------o(___)-
 /  |  \  /  ________/8'
 |  |       /         "
 |  /      |""")

        slowprint("""\nYou pull out a gun and point it towards the cashier...
She puts her hands in the air in chock and you begin smiling...
You--Hand over the money bi**h!
With shaking hands the cashier begins piling the money onto the counter...
You keep pointing your gun to further traumatise the poor woman now begging for her life
Cashier--Please mister! This is a starbucks!\n
Choice 1: Kill the cashier
Choice 2: Spare and take money
Choice 3: Further escalate the situation by pointing your gun at the other clientel
Choice 4: Kill yourself?""")

        while True:
            val=input()
            if val=="1":
                self.kill()
                return
            elif val=="2":
                self.spare()
                return
            elif val=="3":
                self.escalate()
                return
            elif val=="4":
                self.die()
                return
            else:
                slowprint("\nThis is not a valid option!")
    
    def cornered(self):
        slowprint("\nYou are cornered...\n\nChoice 1: Give up\nChoice 2: Kill yoursef")
        while True:
            val=input()
            if val=="1":
                self.lose()
            elif val=="2":
                self.die()
                return
            else:
                slowprint("\nThis is not a valid option!")

    def respect(self):
        print("""
██████╗░███████╗░██████╗██████╗░███████╗░█████╗░████████╗
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝
██████╔╝█████╗░░╚█████╗░██████╔╝█████╗░░██║░░╚═╝░░░██║░░░
██╔══██╗██╔══╝░░░╚═══██╗██╔═══╝░██╔══╝░░██║░░██╗░░░██║░░░
██║░░██║███████╗██████╔╝██║░░░░░███████╗╚█████╔╝░░░██║░░░
╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░░░░╚══════╝░╚════╝░░░░╚═╝░░░""")

    def kill(self):
        slowprint2("\nKilling cashier...")
        slowprint("""\nYou have succefully killed the cashier and now start running toward the front door...
You dart down an empty alleyway whilst hearing sirens closing in...""")
        self.cornered()
        
    def spare(self):
        pass

    def escalate(self):
        slowprint("""\nYou decide to point your gun at the other clientel behind the counter...
""") #continue here!

    def die(self):
        slowprint2("\nW A S T E D")
    
    def lose(self):
        slowprint("""\nYou are arrested by the cops and are now facing charges of attempting murder and robbery...
Days go buy and you now get to choose a lawyer to defend you in court...\n\nChoice 1: Woman\nChoice 2: Man""")
        val=input()
        while True:
            if val=="1":
                self.woman_lawyer()
                return
            elif val=="2":
                self.man_lawyer()
                return
            else:
                slowprint("\nThis is not a valid option!")


    def woman_lawyer(self):
        slowprint("\nYou loose in court and are sentenced to 69 years in jail for attempted robbery and armed offence")

    def man_lawyer(self):
        slowprint("""\nThe date is 12th of January 2023, 2 months since the incident and its time to face the judge...
The judge screams in frustration...
Judge--Order! Order!
The judge ask your lawyer to pledge you case...
Your honor, my client:""")
        self.name=input()
        slowprint(f"""\n{self.name} has simply taken inspiration from the one and only top-G
Andrew Tate in his quest in becoming a \"REAL MAN\"!
Is it so wrong to be such a chad that you kill the woman?
Judge--You've got a point there my friend, that w**re did not give you a \"very handsome boi discount\"
Lawyer--Exacly my point!
Judge--I dont believe that there is anyon in this room that does not respect this fine bois actions
Judge--I herby without any furthere influence of the jury declare you free to go, and i will
personally support you in you battles against bimbos with a check of 2 000 000 dollars""")

        self.respect()