# self is   which represent the current object of class. it allow each object to access its own attributes and methods.
#it is not a keyword like if , elif etc. 
class Car:
    def __init__(abc,brand,model):
        abc.model=model
        abc.brand=brand

Car1 = Car("Toyota","Fortuner")
print(Car1 . model )
print(Car1 . brand )
#  here at the place of self we have used abc . python  doesn't require the word to be self only . its only a standard convention. 
 
