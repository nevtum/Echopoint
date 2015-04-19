from echopoint.messaging import CallbackRegistry

import unittest

class Callback_tests(unittest.TestCase):
    def setUp(self):
        self.registry = CallbackRegistry()
        self.target = Helperclass(self.registry)

    def test_should_publish_without_args(self):
        self.registry.publish('aTopic1')
        self.assertEqual(self.target.methods_invoked(), (True, False))
        self.registry.publish('aTopic2')
        self.assertEqual(self.target.methods_invoked(), (True, True))
        self.assertEqual(self.target.args(), ())
        self.assertEqual(self.target.kwargs(), {})

    def test_should_not_handle_after_unsubscribing_all_from_topic(self):
        self.registry.unsubscribe_all_from('aTopic2')
        self.registry.publish('aTopic2')
        self.assertEqual(self.target.args(), None)
        self.assertEqual(self.target.kwargs(), None)
        self.assertEqual(self.target.methods_invoked(), (False, False))

    def test_should_not_handle_after_unsubscribing_specific_callback(self):
        self.target.unsubscribe_method_1()
        self.registry.publish('aTopic1')
        self.assertEqual(self.target.args(), None)
        self.assertEqual(self.target.kwargs(), None)
        self.assertEqual(self.target.methods_invoked(), (False, False))

    def test_should_publish_with_args_payload(self):
        self.registry.publish('aTopic1', 2, 4, 6)
        self.assertEqual(self.target.args(), (2, 4, 6))
        self.assertEqual(self.target.kwargs(), {})
        self.assertEqual(self.target.methods_invoked(), (True, False))

    def test_should_publish_with_kwargs_payload(self):
        self.registry.publish('aTopic2',
                               aggregate_id=123,
                               message="my message")

        kwargs = self.target.kwargs()
        self.assertEqual(kwargs['aggregate_id'], 123)
        self.assertEqual(kwargs['message'], "my message")
        self.assertEqual(self.target.methods_invoked(), (False, True))

    def test_should_publish_with_args_and_kwargs(self):
        self.registry.publish('aTopic1', 2, 4, 6,
                               aggregate_id=123,
                               message="my message")

        self.assertEqual(self.target.args(), (2, 4, 6))
        kwargs = self.target.kwargs()
        self.assertEqual(kwargs, {'aggregate_id':123, 'message':"my message" })
        self.assertEqual(self.target.methods_invoked(), (True, False))

class Helperclass(object):
    def __init__(self, publisher):
        self._args = None
        self._kwargs = None
        self._method1_invoked = False
        self._method2_invoked = False
        self.publisher = publisher
        self.publisher.subscribe('aTopic1', self._method_1)
        self.publisher.subscribe('aTopic2', self._method_2)

    def _method_1(self, *args, **kwargs):
        self._method1_invoked = True
        self._args = args
        self._kwargs = kwargs

    def _method_2(self, *args, **kwargs):
        self._method2_invoked = True
        self._args = args
        self._kwargs = kwargs

    def unsubscribe_method_1(self):
        self.publisher.unsubscribe('aTopic1', self._method_1)

    def methods_invoked(self):
        return self._method1_invoked, self._method2_invoked

    def args(self):
        return self._args

    def kwargs(self):
        return self._kwargs
