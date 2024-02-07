from display.observer import Observer


class ExcitedDisplay(Observer):
    def __init__(self):
        self.name = "Excited Display"

    def update(self, subject) -> None:
        print(f"Yipee! The stock price is: {subject.price}")
