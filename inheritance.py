# it allows a class to acquire properties and methods of another class.
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} is starting...")
class Bike(Vehicle): # inherit from vehicle
    
    def __init__(self,brand):
        super().__init__(brand)
    def ride(self):
        print(f"{self.brand} is being ridden.")
bike = Bike("Yamaha")
bike.start()
bike.ride()
#