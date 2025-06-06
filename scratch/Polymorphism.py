#try polymorphism example

print("Polymorphism Example")
class Vehicle:
    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"{self.brand} {self.model}"
    def move(self):
        print("Move!")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

class Boat(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def move(self):
        print("Sail!")
class Airplane(Vehicle):
    def __init__(self, brand,model):
        super().__init__(brand, model)
    def __str__(self):
        return f"-->{self.brand} {self.model}"
    def move(self):
        print("Fly!")
v1 = Vehicle("Generic", "Model")

car1 = Car("Toyota", "Corolla")
boat1 = Boat("Yamaha", "242X")
airplane1 = Airplane("Boeing", "747")

#Test polymorphism

for tt in (Car("Toyota", "Corolla"), Boat("Yamaha", "242X"), Airplane("Boeing", "747")):
    print(tt)
    print(tt.move())





#test

class Person:
    def __init__(self, name,lastname):
        self.name = name
        self.lastname = lastname

p1 = Person("John", "Doe")
p2 = Person("Jane", "Smith")
# Test polymorphism
print(p1.name)
print(p2.name)

input("Press Enter to exit")