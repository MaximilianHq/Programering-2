from abc import ABC, abstractmethod
from colorama import Fore, Back, Style
import copy

class Product(ABC):

  def __init__(self, name, price):
    self.name = name
    self.price = price

  @abstractmethod
  def addItem(self):
    pass
  


class Coffee (Product):
  def __init__(self, name, price):
    super().__init__(name, price)
    self.sizes = list()

  def addSize(self, size, price):
    self.sizes.append((size, price))


  def displaySizes(self):
    for size in self.sizes:
      print(f"\n{size[0]} : {size[1]}kr\n")

  #Fråga efter storlek
  def addItem(self):
    
    if(len(self.sizes) == 0):
      return
    
    self.displaySizes()

    while True:
      sizeSelect = input("Vilken storlek vill du ha?: ")
      
      for size in self.sizes:
        if(sizeSelect == size[0]):
          self.price = size[1]
          self.name = size[0] + self.name
          return
          
      else: 
        print(f"{sizeSelect} är inte ett giltig storlek!")

class Cake(Product):
  def __init__(self, name, price):
    super().__init__(name, price)

  def addItem(self):
    pass
    
  


class Customer:
  def __init__(self, budget):
    self.items = list()
    self.budget = budget
    self.activeItem = 0

  def addItem(self, product, amount):
    self.items.append((product, amount))

  def getTotal(self):
    sum = 0
    for item in self.items:
      sum += item[0].price * item[1]

    return sum
    
  
  
  def removeItem(self):
    
    self.printItems()
    while(True):
      try:
        itemIndex = int(input("\nVilken vara vill du ta bort?: "))
      except:
        print("Skriv ett giltig nummer!\n")
        

      productIndex = itemIndex-1

      if productIndex > len(self.items):
        continue
      
      self.activeItem = productIndex

      self.printItems()

      inputText = input("Ta bort den här varan?: Y/N: ")

      if(inputText =="Y"):
        break
      else:
        return
      

    self.budget += self.items[productIndex][0].price *   self.items[productIndex][1]
    self.items.pop((productIndex))
    
    self.printItems()

  def printItems(self):
    print(Fore.RED + "\nDINA VAROR\n------------------------\n" + Fore.WHITE)
    for index, item in enumerate(self.items):
      if(index == self.activeItem):
        print(Back.RED + f"Nr{index + 1} : {item[1]} st {item[0].name} för {item[0].price * item[1]}kr" + Back.RESET + "\n")
        
      else:
        print(f"Nr{index + 1} : {item[1]} st {item[0].name} för {item[0].price * item[1]}kr\n")
      

    print(Fore.RED + "------------------------\n" +Fore.WHITE)


class menu:
  def __init__(self):
    self.products = list()

    #Skapa kaffe fån kaffe klass
    espresso = Coffee("kaffe", 10)

    #Lägg till storlek med olika priser
    espresso.addSize("liten", 10)
    espresso.addSize("medium", 12)
    espresso.addSize("stor", 15)

    #Lägg till produkten i menyn.
    self.products.append(espresso)

    latte = Coffee("latte", 13)
    latte.addSize("liten", 13)
    latte.addSize("mellan", 15)
    self.products.append(latte)

    varmchoklad = Coffee("varmchoklad", 15)
    varmchoklad.addSize("liten", 15)
    varmchoklad.addSize("mellan", 18)
    self.products.append(varmchoklad)

    vatten = Coffee("vatten", 5)
    self.products.append(vatten)

    cake = Cake("cake", 20)
    self.products.append(cake)
    
    

  #Kolla om något finns på menyn.
  def checkInStock(self, productCheck):
    for index, product in enumerate(self.products):
      if product.name == productCheck:
        return index

    else: return "null"


  def getItem(self, itemIndex):
    return self.products[itemIndex]



class Cafe:    

  def printMenu(self):
    print("    MENY\n------------\n")
    for item in self.menu.products:
      print(f"{item.name} : {item.price}kr\n")

    print("------------\n")
  
  def __init__(self):
    self.menu = menu()
    

  def takeOrder(self, budget):
    finishedOrdering = False
    customer = Customer(budget)

    print("Välkommen till Oopcafe!\n")

    self.addItem(customer)
    
    while(finishedOrdering == False):

      customer.printItems()
      print(f"Summan är {customer.getTotal()}kr")
      
      
      print("\nSkriv 1 för att utför köpet")
      print("\nSkriv 2 för att ta bort en vara")
      print("\nSkriv 3 för att lägga till en vara")
      inputPrompt = input("\nVad vill du göra?: ")

      if(inputPrompt == "1"):
        finishedOrdering = True
      elif(inputPrompt == "2"):
        customer.removeItem()
      elif(inputPrompt == "3"):
        self.addItem(customer)
      
  
  def addItem(self, customer):
    print(f"\nPengar kvar: {customer.budget}\n")
      
    self.printMenu()
    
    item = input("Vad vill du ha?: ").lower()  
     
    itemIndex = self.menu.checkInStock(item)
    
    if(itemIndex == "null"):
      print("Finns inte i vår meny!")
      return

    item = copy.copy(self.menu.getItem(itemIndex))
    item.addItem()

    #Fråga efter antalet de vill köpa
    while(True):
      try:
        amount = int(input("\nHur många vill du ha?: "))
      except:
        print("Please type an amount!\n")
        continue

      break
    
    if((customer.budget - item.price * amount) < 0):
      print(f"\nDu har inte råd! Du har bara {customer.budget} kr kvar!\n")
      return
    
    customer.addItem(item, amount)
    customer.budget -= item.price * amount



      
    
    
  