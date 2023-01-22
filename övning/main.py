class Item:
    pay_rate=0.8
    def __init__(self, name:str, price:float, quant=0):
        print(f"product : {name, price, quant}")
        
        assert price >= 0, f"price: {price}, is not a possetive number"

        self.name=name
        self.price=price
        self.quantity=quant

    def calculate_total_price(self):
        pass

item1=Item("phone", 100)
item2=Item("laptop", 1000, 3)

item2.has_battery=True
print(item2.has_battery)