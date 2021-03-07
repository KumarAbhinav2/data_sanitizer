import abc


class JsonSanitizerInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_json(self, in_json):
        pass
