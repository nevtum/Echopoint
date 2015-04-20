import logging

class CallbackRegistry:
    def __init__(self):
        self._subscriptions = {}
        self.logger = logging.getLogger()
        self.executing = []

    def subscribe(self, topic, callback):
        self.logger.info("subcribing to %s." % topic)
        if topic not in self._subscriptions:
            self._subscriptions[topic] = []

        if callback in self._subscriptions[topic]:
            self.logger.warning("attempting to subscribe callback more than once.")
            return

        self._subscriptions[topic].append(callback)

    def unsubscribe_all_from(self, topic):
        self.logger.info("unsubcribing all callbacks from %s." % topic)
        self._subscriptions[topic] = []

    def unsubscribe(self, topic, callback):
        self.logger.info("unsubcribing callback from %s." % topic)
        self._subscriptions[topic].remove(callback)

    def total_subscriptions(self, topic):
        if topic not in self._subscriptions:
            return 0

        return len(self._subscriptions[topic])

    def publish(self, topic, *args, **kwargs):
        if topic in self.executing:
            error = "recursive call violation, topic '%s'" % topic
            self.logger.error(error)
            raise RuntimeError(error)

        self.executing.append(topic)

        for func in self._subscriptions[topic]:
            func(*args, **kwargs)

        self.executing.remove(topic)

class EventPublisher:
    """ A callback registry facade. """
    def __init__(self):
        self._registry = CallbackRegistry()

    def subscribe(self, event_type, callback):
        self._registry.subscribe(self._class_qualified_name(event_type), callback)

    def unsubscribe(self, event_type, callback):
        self._registry.unsubscribe(self._class_qualified_name(event_type), callback)

    def unsubscribe_all_from(self, event_type):
        self._registry.unsubscribe_all_from(self._class_qualified_name(event_type))

    def publish(self, event_obj):
        self._registry.publish(self._obj_qualified_name(event_obj), event_obj)

    def _class_qualified_name(self, event_type):
        return '%s.%s' % (event_type.__module__, event_type.__qualname__)

    def _obj_qualified_name(self, event_obj):
        return '%s.%s' % (event_obj.__module__, event_obj.__class__.__qualname__)
