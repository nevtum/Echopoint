from echopoint.messaging import CallbackRegistry

import unittest

class Subscription_tests(unittest.TestCase):
    def setUp(self):
        self.publisher = CallbackRegistry()

    def test_should_subscribe_two_callbacks_to_same_topic(self):
        self.assertEqual(self.publisher.total_subscriptions('aTopic'), 0)
        self.publisher.subscribe('aTopic', self.my_callback)
        self.assertEqual(self.publisher.total_subscriptions('aTopic'), 1)
        self.publisher.subscribe('aTopic', self.my_second_callback)
        self.assertEqual(self.publisher.total_subscriptions('aTopic'), 2)

    def test_should_subscribe_callback_once_to_same_topic(self):
        self.publisher.subscribe('aTopic', self.my_callback)
        self.publisher.subscribe('aTopic', self.my_second_callback)
        self.assertEqual(self.publisher.total_subscriptions('aTopic'), 2)
        self.publisher.subscribe('aTopic', self.my_callback)
        self.assertEqual(self.publisher.total_subscriptions('aTopic'), 2)
        self.publisher.subscribe('aTopic', self.my_second_callback)
        self.assertEqual(self.publisher.total_subscriptions('aTopic'), 2)

    def test_should_subscribe_callbacks_to_separate_topics(self):
        self.assertEqual(self.publisher.total_subscriptions('aTopic1'), 0)
        self.assertEqual(self.publisher.total_subscriptions('aTopic2'), 0)
        self.publisher.subscribe('aTopic1', self.my_callback)
        self.assertEqual(self.publisher.total_subscriptions('aTopic1'), 1)
        self.assertEqual(self.publisher.total_subscriptions('aTopic2'), 0)
        self.publisher.subscribe('aTopic2', self.my_second_callback)
        self.assertEqual(self.publisher.total_subscriptions('aTopic1'), 1)
        self.assertEqual(self.publisher.total_subscriptions('aTopic2'), 1)

    def test_should_unsubscribe_two_callbacks_from_same_topic(self):
        self.publisher.subscribe('aTopic', self.my_callback)
        self.publisher.subscribe('aTopic', self.my_second_callback)
        self.assertEqual(self.publisher.total_subscriptions('aTopic'), 2)
        self.publisher.unsubscribe_all_from('non-existant-topic')
        self.assertEqual(self.publisher.total_subscriptions('aTopic'), 2)
        self.publisher.unsubscribe_all_from('aTopic')
        self.assertEqual(self.publisher.total_subscriptions('aTopic'), 0)

    def test_should_throw_exception_when_unsubscribing_from_non_existant_topic(self):
        unregister = self.publisher.unsubscribe
        callback = self.my_callback
        self.assertRaises(KeyError, unregister, 'non-existant-topic', callback)

    def test_should_unsubscribe_specific_callback_from_topic(self):
        self.publisher.subscribe('aTopic', self.my_callback)
        self.publisher.subscribe('aTopic', self.my_second_callback)
        self.assertEqual(self.publisher.total_subscriptions('aTopic'), 2)
        self.publisher.unsubscribe('aTopic', self.my_callback)
        self.assertEqual(self.publisher.total_subscriptions('aTopic'), 1)

    def my_callback(self):
        pass

    def my_second_callback(self):
        pass
