class Triangle:
    def __init__(self,side1,side2,side3):
         self.side1=side1
         self.side2=side2
         self.side3=side3
    
    def biggest_side(self):
        sides=[self.side1,self.side2,self.side3]
        bigg_side= max(sides)
        print(f"El mayor lado mide una longitud de : {bigg_side}")

    def return_type_triangle(self) :
        if self.side1==self.side2==self.side3:
            return "equilatero"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "isosceles"
        else:
          return "escaleno"
            
            