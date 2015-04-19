from tests.subscriptions import Subscription_tests
from tests.messaging import Event_publisher_tests
from tests.callbacks import Callback_tests
from tests.shortcut_subscriptions import Decorator_tests

import unittest
import logging

def configure_logger():
    handler = logging.FileHandler('log.txt')
    formatter = logging.Formatter("%(asctime)s [%(threadName)s] [%(levelname)s]  %(message)s")
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)

if __name__ == '__main__':
    configure_logger()
    unittest.main()
