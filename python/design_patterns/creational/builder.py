'''
Builder pattern aims to “Separate the construction of a complex object from its representation so that the same
construction process can create different representations.” It is used to construct a complex object step by step
and the final step will return the object. The process of constructing an object should be generic so that it can be
used to create different representations of the same object.
Complex Object: Pizza (consists of crust, sauce, toppings )
We can have different types of pizza based on different build steps (eg: different crust, different sauce, toppings etc).
Some may have toppings and some may nt have any toppings.
Pizza                       PizzBuilder                                 Waiter
-set crust                  /         \                             Take order for any type of pizza (SpicyPizzaBuilder)
-set sauce        SpicyPizzaBuilder   CheesePizzaBuilder              SpicyPizzaBuilder.make_pizza
-set toppings      Create New Pizza    Create New Pizza               SpicyPizzaBuilder.get_pizza
                    Set spicy sauce     Set ceese toppings
                    Set crust
'''
from abc import ABC, abstractmethod
class Pizza(object):

    def __init__(self):
        self.crust = None
        self.sauce = None
        self.toppings = None

    def __str__(self):
        return "-".join([self.crust, self.sauce, self.toppings])


class PizzaBuilder(ABC):

    def __init__(self):
        self.pizza = None

    def create_pizza(self):
        self.pizza = Pizza()

    def get_pizza(self):
        return self.pizza

    @abstractmethod
    def set_sauce(self):
        pass

    @abstractmethod
    def set_crust(self):
        pass

    @abstractmethod
    def set_toppings(self):
        pass


class SpicyPizzaBuilder(PizzaBuilder):

    def set_sauce(self):
        self.pizza.sauce = "spicy Sauce"

    def set_crust(self):
        self.pizza.crust = "thin crust"

    def set_toppings(self):
        self.pizza.toppings = "capsicum"


class CheesePizzaBuilder(PizzaBuilder):

    def set_sauce(self):
        self.pizza.sauce = "sweet Sauce"

    def set_crust(self):
        self.pizza.crust = "thin crust"

    def set_toppings(self):
        self.pizza.toppings = "extra cheese"


class Chef(object):

    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        self.builder.create_pizza()
        self.builder.set_crust()
        self.builder.set_sauce()
        self.builder.set_toppings()

    def get_pizza(self):
        return self.builder.get_pizza()


if __name__ == '__main__':
    spicy_pizza_builder = CheesePizzaBuilder()
    chef = Chef(spicy_pizza_builder)
    chef.make_pizza()
    pizza = chef.get_pizza()
    print(pizza)



