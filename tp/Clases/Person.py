class Person:
    def __init__(self):
        pass
    
    def self_name(self,name):
        self.name=name
    def self_age(self,age):
        self.age=age
    def self_dni(self,dni):
        self.dni=dni
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_dni(self):
        return self.dni
    def show(self):
        print(f"El nombre es :{self.name}")
        print(f"Tiene una edad de {self.age}")
        print(f"y su dni es : {self.dni}")
    def is_legal(self):
        if self.age>=18:
           return True
        else:
            return False