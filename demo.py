import sys

from us_visa.logger import logging
from us_visa.exception import USvisaException


logging.info("This is an info message")

try:
    a = 1 / 0
except Exception as e:
    logging.error("An error occurred: %s", str(e))
    raise USvisaException(e, sys)
