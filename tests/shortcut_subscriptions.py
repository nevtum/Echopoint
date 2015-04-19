from echopoint import shortcuts

import unittest

handles_triggered = []

class Decorator_tests(unittest.TestCase):
    def setUp(self):
        global handles_triggered
        handles_triggered = []

    def test_decorator_works(self):
        shortcuts.publish(AccountCreated())
        self.assertEqual('handler1' in handles_triggered, True)
        self.assertEqual('handler2' in handles_triggered, True)
        self.assertEqual('handler3' in handles_triggered, False)

    def test_other_decorator_works(self):
        shortcuts.publish(CargoDelivered())
        self.assertEqual('handler1' in handles_triggered, False)
        self.assertEqual('handler2' in handles_triggered, False)
        self.assertEqual('handler3' in handles_triggered, True)

''' an example event part of
    a specific domain '''
class AccountCreated:
    pass

''' an example event part of
    a specific domain '''
class CargoDelivered:
    pass

@shortcuts.handle(AccountCreated)
def handler1(obj):
    handles_triggered.append('handler1')

@shortcuts.handle(AccountCreated)
def handler2(obj):
    handles_triggered.append('handler2')

@shortcuts.handle(CargoDelivered)
def handler3(obj):
    handles_triggered.append('handler3')
