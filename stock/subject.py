from abc import ABC, abstractmethod


class Subject(ABC):
    """Subject notifies observers about changes"""

    def __init__(self):
        self.observers = []

    @abstractmethod
    def attach(self, observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass
