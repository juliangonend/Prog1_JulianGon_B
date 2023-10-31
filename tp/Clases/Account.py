class  Account :
    
    def __init__(self,titular,quantity=0.00):
        self.titular=titular,
        self.quantity=quantity
    
    def set_titular(self,name):
        self.name=name
        
    def self_quantity(self,quantity):
        self.quantity=quantity
    
    def get_titular(self):
        return self.titular
    def get_quantity(self):
        return self.quantity
    def show(self):
        print(f"La cuenta del titular : {self.titular} tiene : ${self.quantity}")
        
    def deposit(self,quantity):
        if quantity >0:
            self.quantity+=quantity
    def withdraw(self,quantity):
        self.quantity-=quantity