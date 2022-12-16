'''
Use the Adapter class when you want to use some existing class, but its interface isn’t compatible with the rest of
your code. The Adapter pattern lets you create a middle-layer class that serves as a translator between your code and a
legacy class, a 3rd-party class or any other class with a weird interface.

Use the pattern when you want to reuse several existing subclasses that lack some common functionality that can’t be
added to the superclass.You could extend each subclass and put the missing functionality into new child classes.
However, you’ll need to duplicate the code across all of these new classes, which smells really bad.
The much more elegant solution would be to put the missing functionality into an adapter class. Then you would wrap
objects with missing features inside the adapter, gaining needed features dynamically. For this to work, the target
classes must have a common interface, and the adapter’s field should follow that interface. This approach looks very
similar to the Decorator pattern.
'''

from abc import ABC, abstractmethod


class MediaPlayer(ABC):

    @abstractmethod
    def play(self, media_file):
        pass


class AdvancedMediaPlayer(ABC):

    @abstractmethod
    def play_adv_media(self, media_file):
        pass


class VlcPlayer(AdvancedMediaPlayer):

    def play_adv_media(self, media_file):
        print("playing vls media....", media_file)


class Mp4Player(AdvancedMediaPlayer):

    def play_adv_media(self, media_file):
        print("playing mp4 media ....", media_file)


class MediaPlayerAdapter(MediaPlayer):

    def __init__(self, audio_type):
        if audio_type == 'vlc':
            self.player = VlcPlayer()
        else:
            self.player = Mp4Player()

    def play(self, media_file):
        self.player.play_adv_media(media_file)


class AudioPlayer(MediaPlayer):

    def play(self, media_file):
        media_type = media_file.split('.')[-1]
        if media_type == 'mp3':
            print("Playing mp3 media ...", media_file)
        else:
            media_adapter = MediaPlayerAdapter(media_type)
            media_adapter.play(media_file)


if __name__ == "__main__":
    audio_player = AudioPlayer()
    audio_player.play("summer of 69.mp3")
    audio_player.play("Rock On.vlc")
    audio_player.play("See you again.mp4")







