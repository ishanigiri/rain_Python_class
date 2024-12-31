from abc import ABC, abstractmethod
class Vehicle(ABC):
    #@abstractmethod
    def drive(self):
        print("Vehicle is driving")
        #pass
    def new_fn(self):
        print("My new fn")
class Car(Vehicle):
    pass
    #def drive(self):
    # return "car is driving"
#example: Using abstraction
car = Car()
print(car.drive())  #output:car is driving

#veh = Vehicle()
#print(Veh.drive()) # Access abstract method
