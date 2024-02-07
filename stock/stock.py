from stock.subject import Subject
import logging


class Stock(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.price = 0

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        self._price = value
        self.notify()

    def notify(self) -> None:
        logging.info("Stock: Price change -  Notifying observers")
        for observer in self.observers:
            observer.update(self)

    def attach(self, observer) -> None:
        print(f"Stock: Attaching Observer: {observer.name} ")
        self.observers.append(observer)

    def detach(self, observer) -> None:
        logging.info("Stock: Detaching Observer")
        self.observers.remove(observer)
