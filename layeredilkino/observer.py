from abc import abstractmethod


class Message:
    pass


class Observer:
    @abstractmethod
    def update(self, _message: Message):
        pass


class Subject:
    @abstractmethod
    def attach(self, _observer: Observer):
        pass

    @abstractmethod
    def detach(self, _observer: Observer):
        pass

    @abstractmethod
    def notify_update(self, _msg: Message):
        pass