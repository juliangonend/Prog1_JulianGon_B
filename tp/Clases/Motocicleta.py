class Motocicleta:
    state="new"
    engine=False
    
    def __init__(self,color,registration,brand,model,
                 manufacturing_date,top_speed,weight,fuel_liters=10,number_wheels=2):
       self.color=color
       self.registration=registration
       self.fuel_liters=fuel_liters
       self.number_wheels=number_wheels
       self.brand=brand
       self.model=model;
       self.manufacturing_date=manufacturing_date
       self.top_speed=top_speed
       self.weight=weight

       
       
    def start_engine(self):
        if self.engine  is not True:
            self.engine=True;
            print(f"El motor de la motocicleta {self.brand} modelo : {self.model} ha arrancado")
        else:
            print(f"El motor de la motocicleta {self.brand} modelo : {self.model} ya esta en marcha  ")
   
    def stop_engine(self):
        if self.engine is True:
            self.engine=False
            print(F" El motor de la motocicleta {self.brand} modelo: {self.model} se ha detenido") 
        else:
            print(f"El motor de la motocicleta {self.brand} del modelo : {self.model} ya estaba detenido")
        
    def check_price(self):
       
        print(f"El precio de la motocicleta {self.brand} modelo {self.model} cuesta {self.price}$")
        # else:
        #     print(f" La moto {self.brand} : {self.model} no tiene precio")