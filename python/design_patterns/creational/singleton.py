


'''
Client should make sure they call only get_instance method to create new instance.
a1,a2=Singleton1.get_instance(),Singleton1.get_instance()
b1,b2=Singleton1(),Singleton1()
print(a1==a2) #o/p: true
print(b1==b2) #o/p: false
'''
class Singleton1(object):
    __instance = None

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance


'''
This will make sure client not able to create multiple instances.
a1,a2=Singleton1(),Singleton1()
print(a1==a2) #o/p: true
'''
class Singleton2(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        cls.__instance = super(cls, cls).__new__(cls, *args, *kwargs)
        return cls.__instance


'''
Thread Safe
'''
from threading import Lock
class Singleton3(object):
    __lock = Lock()
    __instance = None

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = cls(*args, **kwargs)
        return cls.__instance

'''
Using Decorator
'''
def singleton(cls):
    instance_cache = {}

    def inner(*args, **kwargs):
        if cls not in instance_cache:
            instance_cache[cls]=cls(*args, **kwargs)
        return instance_cache[cls]
    return inner

@singleton
class MyClass(object):
    pass

@singleton
class MyAnotherClass(object):
    pass


a1, a2 = MyClass(), MyClass()
b1, b2 = MyAnotherClass(), MyAnotherClass()
print("a1==a2 : ", a1 == a2)
print("b1==b2 : ", b1 == b2)
print("a1==b1 : ", a1 == b1)

'''
We can also use metaclass to provide singleton feature
'''