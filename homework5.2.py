# Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child classes
class Cow(Animal):
    def moo(self):
        print(f"{self.name} says 'Moo!'")

class Chicken(Animal):
    def cluck(self):
        print(f"{self.name} says 'Cluck!'")

class Pig(Animal):
    def oink(self):
        print(f"{self.name} says 'Oink!'")

# Demonstrate the farm
cow = Cow("Bessie", 5)
chicken = Chicken("Clucky", 2)
pig = Pig("Por", 3)

# Actions
print("Farm animals in action:")
cow.eat()
cow.moo()

chicken.eat()
chicken.cluck()

pig.eat()
pig.oink()