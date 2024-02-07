import logging

from display.excited_display import ExcitedDisplay
from stock.stock import Stock
from display.display import Display

logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)
logger.setLevel("INFO")

logger.info("Initializing program")

stock = Stock()
display = Display()
excited_display = ExcitedDisplay()

stock.attach(display)
stock.attach(excited_display)

stock.price = 5
stock.price = 12
stock.price = 15
stock.price = 25
