'''
The Strategy pattern suggests that you take a class that does something specific in a lot of different ways and extract
all of these algorithms into separate classes called strategies.
The original class, called context, must have a field for storing a reference to one of the strategies. The context
delegates the work to a linked strategy object instead of executing it on its own.
The context isn’t responsible for selecting an appropriate algorithm for the job. Instead, the client passes the desired
strategy to the context. In fact, the context doesn’t know much about strategies. It works with all strategies through
the same generic interface, which only exposes a single method for triggering the algorithm encapsulated within the
selected strategy.This way the context becomes independent of concrete strategies, so you can add new algorithms or
modify existing ones without changing the code of the context or other strategies.
'''

from abc import ABC, abstractmethod


class SortingStrategy(ABC):

    @abstractmethod
    def sort(self,data):
        pass


class MergeSort(SortingStrategy):

    def sort(self, data):
        print("doing merge sort on data ...")


class QuickSort(SortingStrategy):

    def sort(self, data):
        print("doing quick sort on data ...")


class CustomerList(object):

    def __init__(self):
        self.customers = []
        self.sorting_strategy = QuickSort()

    def set_sorting_strategy(self, strategy):
        self.sorting_strategy = strategy

    def add_customer(self, name):
        self.customers.append(name)

    def do_something(self):
        print("Doing Something ...")
        self.sorting_strategy.sort(self.customers)
        print("Task complete...")


if __name__ == "__main__":
    all_customers = CustomerList()
    all_customers.add_customer('Hari')
    all_customers.add_customer('Roky')
    all_customers.add_customer('Adam')
    all_customers.do_something()

    sorting_strategy = MergeSort()
    all_customers.set_sorting_strategy(sorting_strategy)
    all_customers.do_something()
