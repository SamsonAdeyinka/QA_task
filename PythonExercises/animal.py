from abc import ABC, abstractmethod

class Animal():
    def __init__(self, type):
        self.type = type
        super(Animal).__init__()

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__("Mammal")
        self.name = name

    def speak(self):
        return "woof"


pet = Dog("Krypto")

print(pet.name)
print(pet.type)
print(pet.speak())
