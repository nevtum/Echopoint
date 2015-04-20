from echopoint.messaging import EventPublisher

_publishers = {}

''' decorator method '''
def handle(EventType, channel="default"):
    def inner(f):
        if channel not in _publishers.keys():
            _publishers[channel] = EventPublisher()
        _publishers[channel].subscribe(EventType, f)
        return f
    return inner

def publish(EventInstance, channel="default"):
    _publishers[channel].publish(EventInstance)
