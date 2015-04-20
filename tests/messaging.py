from echopoint.messaging import EventPublisher
from echopoint.events import DomainEvent

import unittest

class Event_publisher_tests(unittest.TestCase):
    def setUp(self):
        self.publisher = EventPublisher()
        self.publisher.subscribe(DomainEvent, self.my_callback)
        self.publisher.subscribe(DomainEvent, self.my_second_callback)
        self.aggregate_id = None
        self.callback1_invoked = False
        self.callback2_invoked = False

    def test_callbacks_should_receive_event(self):
        self.publisher.publish(DomainEvent(12345))
        self.assertEqual(self.aggregate_id, 12345)
        self.assertEqual(self.callback1_invoked, True)
        self.assertEqual(self.callback2_invoked, True)

    def test_callback2_should_not_receive_event(self):
        self.publisher.unsubscribe(DomainEvent, self.my_second_callback)
        self.publisher.publish(DomainEvent(54321))
        self.assertEqual(self.aggregate_id, 54321)
        self.assertEqual(self.callback1_invoked, True)
        self.assertEqual(self.callback2_invoked, False)

    def test_callbacks_should_not_receive_event(self):
        self.publisher.unsubscribe_all_from(DomainEvent)
        self.publisher.publish(DomainEvent(11111))
        self.assertEqual(self.aggregate_id, None)
        self.assertEqual(self.callback1_invoked, False)
        self.assertEqual(self.callback2_invoked, False)

    def test_should_not_allow_recursive_calls(self):
        self.assertRaises(RuntimeError, expected_runtime_exception)

    def my_callback(self, event_obj):
        self.callback1_invoked = True
        self.aggregate_id = event_obj.aggregate_id

    def my_second_callback(self, event_obj):
        self.callback2_invoked = True

def expected_runtime_exception():
    publisher = EventPublisher()

    def cb1(obj):
        publisher.publish(DomainEvent(99999))

    publisher.subscribe(DomainEvent, cb1)
    publisher.publish(DomainEvent(22222))
