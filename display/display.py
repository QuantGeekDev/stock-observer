from display.observer import Observer


class Display(Observer):
    def __init__(self):
        self.name = "Display"

    def update(self, subject):
        if subject is not None:
            stock_price = subject.price
            print(f"Stock Price: {stock_price}")
