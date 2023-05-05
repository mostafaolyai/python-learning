from abc import ABC, abstractmethod


class Stream(ABC):  # make it abstract class for limit inheritance
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise ValueError('stream is already open')
        self.opened = True

    def close(self):
        if not self.opened:
            raise ValueError('stream is already close')
        self.opened = False

    @abstractmethod  # make it force to implement in inherited class
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print('file stream reading')


# stream = Stream()  # TypeError: Can't instantiate abstract class Stream with abstract method read

# not implemented read
class NetworkStream(Stream):
    pass
