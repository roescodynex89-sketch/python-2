# Create a Product class with name and price. Create two objects and print their information.

class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def show_info(self):
        print(self.name,self.price)

product1=product("laptop",5555555)
product2=product("os",5555)

product1.show_info()