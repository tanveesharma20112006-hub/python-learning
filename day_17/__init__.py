# a constructor is a special method in python that runs automatically when an object is created . mainly used to initialize object attributes
class Car:
    def __init__(self,brand,model):
        self.model=model
        self.brand=brand

Car1 = Car("Toyota","Fortuner")
print(Car1 . model )
print(Car1 . brand )

# when we write : 
# Car1 = Car("Toyota","Fortuner")
#python automatically calls __init__(car1,"Toyota","Fortuner")
#then self.brand = brand / create an attribute
#car1.brand = "toyota", car1.model = "Fortuner"

#if we didn't use constructor we have to manually add values. 
# class Car:
# pass
# car1.= Car()
# Car1.brand = "Toyota" 