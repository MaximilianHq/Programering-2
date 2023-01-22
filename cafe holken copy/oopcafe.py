import sys, time, random

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./25) #change the denominators value to change type speed
  
class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        
    def addItem():
        pass
    
class Menu:
    def __init__(self):
        self.products = list()
        
        coffee = Coffee("coffee", 10)
        coffee.add_size("small", 10)
        coffee.add_size("medium", 20)
        coffee.add_size("large", 30)
        self.products.append(coffee)
        
        espresso = Coffee("espresso", 15)
        espresso.add_size("small", 15)
        espresso.add_size("medium", 25)
        self.products.append(espresso)
        
        pie = Pie("pie", 40)
        pie.add_type("cherry", 40)
        pie.add_type("apple", 40)
        pie.add_type("raspberry", 40)
        self.products.append(pie)
        
    def verify_stock(self, choice):
        for index, item in enumerate(self.products):
            if item==choice:
                return index
        else:
            return "null"
            
    def getItemInStock(self, index):
        return self.products[index]
        

class Coffee (Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.size = list()
    
    def add_item(self, name, price):
        print("What size would you like your coffee?")
        size = input()
        
    def add_size(self, name, price):
        self.size.append((name, price))
    
class Pie (Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type = list()
        
    def add_type(self, name, price):
        self.type.append((name, price))
        
    def add_item(self):
        pass
    
class Cashier:
    def __init__(self, cash):
        self.cash=cash
        
class Customer:
    def __init__(self):
        self.cart=()
    
class Cafe():
    def __init__(self):
        self.menu=Menu()
        
    def order(self):
        #take order
        slowprint("What would you like to order?")
        
        for item in self.menu.products:
            print(f"{item.name} : {item.price}")
            
        choice = input()
        choiceIndex = self.menu.verify_stock(choice)
        if choiceIndex != "null":
            product = self.menu.getItemInStock(choiceIndex)
            
        product.add_item()
        
        
        Customer.cart.append()
        

    print("sdasdas")