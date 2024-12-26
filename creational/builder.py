# Design Patterns - Creational - Builder

# Separate the construction of a complex object from its representation so that the same construction process can create different representations.

# Applicability: Use the Builder pattern when:
# - the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled
# - the construction process must allow different representations for the object that's constructed

from abc import ABC, abstractmethod


# Product
class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.toppings = []

    def __str__(self):
        return f"Pizza with {self.dough} dough, {self.sauce} sauce, and toppings: {', '.join(self.toppings)}"


# Abstract Builder
class PizzaBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_dough(self):
        pass

    @abstractmethod
    def build_sauce(self):
        pass

    @abstractmethod
    def build_toppings(self):
        pass

    @abstractmethod
    def get_pizza(self) -> Pizza:
        pass


# Concrete Builder
class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def reset(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.dough = "thin crust"

    def build_sauce(self):
        self.pizza.sauce = "tomato"

    def build_toppings(self):
        self.pizza.toppings = ["mozzarella", "basil"]

    def get_pizza(self) -> Pizza:
        return self.pizza


# Director
class Waiter:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> PizzaBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: PizzaBuilder):
        self._builder = builder

    def construct_pizza(self):
        self.builder.reset()
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_toppings()


# Usage example
if __name__ == "__main__":
    waiter = Waiter()
    margherita_builder = MargheritaPizzaBuilder()

    waiter.builder = margherita_builder
    waiter.construct_pizza()

    pizza = margherita_builder.get_pizza()
    print(
        pizza
    )  # Pizza with thin crust dough, tomato sauce, and toppings: mozzarella, basil
