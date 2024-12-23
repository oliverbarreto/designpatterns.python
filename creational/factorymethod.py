# Design Patterns - Structural - Factory Method (Virtual Constructor)

# Define an interface for creating an object, but let subclasses decide which class to instantiate
# Applicability: Use the Factory Method pattern when:
# - a class can't anticipate the class of objects it must create
# - a class wants its subclasses to specify the objects it creates
# - classes delegate responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper subclass is the delegate


from abc import ABC, abstractmethod


# Animal interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Concrete Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Factory Method or Virtual Creator interface
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

    def make_animal_speak(self):
        animal = self.create_animal()
        return animal.speak()


# Concrete Factories or creators
class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()


# Usage example
if __name__ == "__main__":
    # Create factories
    dog_factory = DogFactory()
    cat_factory = CatFactory()

    # Create and use animals through factories
    print(dog_factory.make_animal_speak())  # Outputs: Woof!
    print(cat_factory.make_animal_speak())  # Outputs: Meow!

    # Direct creation of animals through factories
    dog = dog_factory.create_animal()
    cat = cat_factory.create_animal()

    print(dog.speak())  # Outputs: Woof!
    print(cat.speak())  # Outputs: Meow!
