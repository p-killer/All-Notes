'''
If we have to change behavior of an object based on its state, we can have a state variable in the Object and use
if-else condition block to perform different actions based on the state.
Code like this is very difficult to maintain because any change to the transition logic may require changing state
conditionals in every method. The problem tends to get bigger as a project evolves. It’s quite difficult to predict
all possible states and transitions at the design stage. Hence, a lean state machine built with a limited set of
conditionals can grow into a bloated mess over time.
'''

from abc import ABC, abstractmethod


class MobileAlertState(ABC):

    @abstractmethod
    def alert(self):
        pass


class Vibration(MobileAlertState):

    def alert(self):
        print("Putting mobile in vibration mode")


class Silent(MobileAlertState):

    def alert(self):
        print("Putting mobile in silent mode")


class NormalMode(MobileAlertState):

    def alert(self):
        print("Normal Mode...")


class AlertStateContext(object):

    def __init__(self):
        self.current_state = NormalMode()

    def set_state(self, state):
        self.current_state = state

    def alert(self):
        self.current_state.alert()


if __name__ == "__main__":
    alert_context = AlertStateContext()
    alert_context.alert()
    vibration_mode = Vibration()
    alert_context.set_state(vibration_mode)
    alert_context.alert()
    silent_mode = Silent()
    alert_context.set_state(silent_mode)
    alert_context.alert()