# object oriented programming is a way of structuring code using classes and object to model real world entities . it help in modularity & scalability.
#classes and object :
#class - Blueprint for creating object
# object - instances of
#  class 
class Car:
    #(class attributes shared by all instances)
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Car:{self.brand}{self.model}")

#creating object
car1 = Car("Toyota","Corolla")
car2 = Car ("Tesla","Model S")
car1.display_info()
car2.display_info()