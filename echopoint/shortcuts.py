from echopoint.messaging import EventPublisher

publisher_global = EventPublisher()

''' decorator method '''
def handle(EventType):
    def inner(f):
        publisher_global.subscribe(EventType, f)
        return f
    return inner

def publish(EventInstance):
    publisher_global.publish(EventInstance)
