class Car:
    # Class attribute (shared by all instances)
    wheels = 4

    def __init__(self, brand, model):
        # Instance attributes (unique to each object)
        self.brand = brand
        self.model = model

    # Instance method
    def display_info(self):
        return f"{self.brand} {self.model} with {Car.wheels} wheels"

    # Class method
    @classmethod
    def change_wheels(cls, count):
        if count > 0:
            cls.wheels = count
        else:
            raise ValueError("Wheel count must be positive")

    # Static method
    @staticmethod
    def honk():
        return "Beep! Beep!"


# Creating objects (instances)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing instance attributes
print(car1.brand)      # Toyota
print(car2.model)      # Civic

# Calling instance method
print(car1.display_info())    # Toyota Corolla with 4 wheels

# Calling class method to change class attribute
Car.change_wheels(6)
print(car1.display_info())    # Toyota Corolla with 6 wheels

# Calling static method
print(Car.honk())             # Beep! Beep!