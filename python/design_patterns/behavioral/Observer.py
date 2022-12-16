'''
Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about
any events that happen to the object they’re observing.
 EvenetPublisher                              Listener                       AnyEventClass
   - listeners list                            - update(msg)                  - EventPublisher
   - subscribe(topic,listener)               /             \                  - for any event:
   - unsubscribe(topic,listener)      EmailListener     LogListener               EventPublisher.notify(topic, msg)
   - notify()
     calls update method of listener
'''

from collections import defaultdict
from abc import ABC, abstractmethod
from logging import Logger


class EventPublisher(object):

    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, topic, listener):
        self.listeners[topic].append(listener)

    def unsubscribe(self, topic, listener):
        self.listeners[topic].remove(listener)

    def notify(self, topic, msg):
        for listener in self.listeners.get(topic):
            listener.update(msg)


class Listener(ABC):

    @abstractmethod
    def update(self,msg):
        pass


class LogListener(Listener):

    def __init__(self):
        self.logger = Logger("xyz")

    def update(self, msg):
        print("logging msg.. ", msg)


class EmailListener(Listener):

    def update(self, msg):
        print("sending email.. ", msg)


class Event(object):

    def __init__(self):
        self.publisher = EventPublisher()

    def login(self):
        # some work
        success = True
        if success:
            self.publisher.notify("login", "login successful")
        else:
            self.publisher.notify("login", "login failed")

    def transaction(self):
        self.publisher.notify("transaction", "transaction done")


if __name__ == "__main__":
    email_listener = EmailListener()
    log_listener = LogListener()
    event = Event()
    event.publisher.subscribe("login", email_listener)
    event.publisher.subscribe("transaction", log_listener)
    event.login()
    event.transaction()
