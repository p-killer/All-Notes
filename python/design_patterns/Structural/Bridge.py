'''
The Bridge pattern lets you split the monolithic class into several class hierarchies. After this, you can change the
 classes in each hierarchy independently of the classes in the others. This approach simplifies code maintenance and
 minimizes the risk of breaking existing code.
'''

from abc import ABC, abstractmethod


class Device(ABC):

    def __init__(self):
        self.volume = 0

    def set_volume(self, percentage):
        self.volume = percentage
        print("Current volume is : ", self.volume)

    def get_volume(self):
        return self.volume


class TV(Device):
    pass


class Radio(Device):
    pass


class Remote(object):

    def __init__(self, device):
        self.device = device

    def volume_up(self):
        new_vol = min(self.device.get_volume()+1, 100)
        self.device.set_volume(new_vol)

    def volume_down(self):
        new_vol = max(self.device.get_volume()-1, 0)
        self.device.set_volume(new_vol)


class AdvancedRemote(Remote):

    def mute(self):
        self.device.set_volume(0)


if __name__ == "__main__":
    tv = TV()
    radio = Radio()
    tv_remote = AdvancedRemote(tv)
    radio_remote = Remote(radio)
    tv_remote.volume_up()
    tv_remote.volume_up()
    tv_remote.mute()

    radio_remote.volume_up()
    radio_remote.volume_down()

