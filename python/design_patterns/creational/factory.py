from abc import ABC, abstractmethod


class Animal(object):

    @abstractmethod
    def food(self):
        pass


class Dog(Animal):

    def food(self):
        return 'biscuit'


class Cat(Animal):

    def food(self):
        return 'milk'


class AnimalFactory(object):

    @staticmethod
    def get_animal(name):
        if name=='cat':
            return Cat()
        elif name=='dog':
            return Dog()


if __name__ == '__main__':

    tom = AnimalFactory.get_animal('cat')
    spike = AnimalFactory.get_animal('dog')

    print('tom eats ', tom.food())
    print('spike eats ', spike.food())


