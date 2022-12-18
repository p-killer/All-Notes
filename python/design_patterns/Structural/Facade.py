'''
A facade is a class that provides a simple interface to a complex subsystem which contains lots of moving parts.
A facade might provide limited functionality in comparison to working with the subsystem directly. However, it
includes only those features that clients really care about.
Having a facade is handy when you need to integrate your app with a sophisticated library that has dozens of features,
but you just need a tiny bit of its functionality.
'''


class VideoFile:

    @staticmethod
    def read(file):
        print("working with file: ", file)
        return file


class OggCompressionCodec:

    def __init__(self):
        self.codec = "ogg_codec"


class MPEG4CompressionCodec:

    def __init__(self):
        self.codec = "mpeg4_codec"


class CodecFactory:

    def extract(self, file):
        print("extracting file: ", file)
        return file


class BitrateReader:

    @staticmethod
    def read(file, coder):
        print("reading ", file, "with coder: ", coder)
        return 'buffer'

    @staticmethod
    def convert(buffer, destination_codec):
        print("converting ", buffer, "to: ", destination_codec)
        return 'result'


class AudioMixer:

    def fix(self, result):
        return result

'''
We create a facade class to hide the framework's complexity behind a simple interface. 
'''


class VideoConverter:

    def convert(self, filename, c):
        file = VideoFile.read(filename)
        source_codec = CodecFactory().extract(file)
        if CodecFactory == "mp4":
            destination_codec = MPEG4CompressionCodec().codec
        else:
            destination_codec = OggCompressionCodec().codec
        buffer = BitrateReader.read(filename, source_codec)
        result = BitrateReader.convert(buffer, destination_codec)
        result = AudioMixer().fix(result)
        return result

'''
Application classes don't depend on a billion classes provided by the complex framework. Also, if you decide to switch 
frameworks, you only need to rewrite the facade class.
'''

class Application:

    @staticmethod
    def main():
        converter = VideoConverter()
        mp4 = converter.convert("funny-cats-video.ogg", "mp4")
        print(mp4)


if __name__ == "__main__":
    Application.main()