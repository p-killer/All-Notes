'''
Abstract Factory offers the interface for creating a family of related objects,
without explicitly specifying their classes
eg:
(Dog, Cat) , (pet,wild)
Possible combination:
(pet,Dog), (pet,Cat), (wild, Dog), (wild,Cat)
       Animal          AnimalFactory
       |   \             /        \
     Cat   Dog        PetFactory   WildFactory
                    Creates petCat  Create WildCat
                            petDog         WildDog
'''
from abc import ABC, abstractmethod


class Animal(object):

    def __init__(self,pet_or_wild):
        self.type = pet_or_wild

    @abstractmethod
    def food(self):
        pass


class Dog(Animal):

    def food(self):
        if self.type=='pet':
            return 'biscuit'
        else:
            return 'meat'


class Cat(Animal):

    def food(self):
        if self.type == 'pet':
            return 'milk'
        else:
            return 'fish'


class AnimalFactory(object):
    pass

class WildAnimalFactory(AnimalFactory):

    @staticmethod
    def get_dog():
        return Dog('wild')

    @staticmethod
    def get_cat():
        return Cat('wild')

class PetAnimalFactory(AnimalFactory):

    @staticmethod
    def get_dog():
        return Dog('pet')

    @staticmethod
    def get_cat():
        return Cat('pet')




class FactoryProvider(object):

    @staticmethod
    def get_factory(name):
        if name=='pet':
            return PetAnimalFactory
        else:
            return WildAnimalFactory


if __name__ == '__main__':

    pet_factory = FactoryProvider.get_factory('pet')
    wild_factory = FactoryProvider.get_factory('wild')

    tom = pet_factory.get_cat()
    spike = pet_factory.get_dog()

    wild_tom = wild_factory.get_cat()
    wild_spike = wild_factory.get_dog()

    print('tom eats ', tom.food())
    print('spike eats ', spike.food())
    print('wild tom eats ', wild_tom.food())
    print('wild spike eats ', wild_spike.food())


