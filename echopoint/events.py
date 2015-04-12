
class DomainEvent(object):
    def __init__(self, aggregate_id):
        self.aggregate_id = aggregate_id
