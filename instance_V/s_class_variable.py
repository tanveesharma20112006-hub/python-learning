# instance variable : a variable that belong to a specific object .
# created by using self.variable
class Car:
    def __init__(self,brand):
        self.brand = brand
car1 = Car("Toyota")
car2 = Car("BMW")
print(car1.brand)
print(car2.brand)
#here each object has diff values


#class variable: a variable that is shared among all object in the same class.
#it is created inside the class but outside methods.
class Car:
    wheel = 4
    def __init__(self,brand):
        self.brand = brand
Car1 = Car("Toyota")
Car2 = Car("BMW")
print(Car1.wheel)
print(Car2. wheel)        

#these 4 , 4 are class variable which are same for all obj.

