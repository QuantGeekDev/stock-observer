from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def __init__(self):
        self.name = ""

    @abstractmethod
    def update(self, subject):
        """Receive an update from the subject"""
