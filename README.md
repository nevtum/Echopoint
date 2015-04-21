# Echopoint

Echopoint is a library aimed to assist developers in writing decoupled
applications by leveraging event publishing using lightweight subscription
mechanisms. The event publisher is often synonymous to the Observer Pattern
(GoF). It's designed to notify subscribers synchronously, therefore it's use
is generally limited to single process applications. In exchange, consistent
and repeatable behavior is guaranteed. It is advised to write
asynchronous event handlers instead to achieve concurrent application design,
however the notification mechanism within Echopoints event publisher is and
always will be synchronous.

Installation
============

Install Echopoint using Pip:

    $ pip install git+https://github.com/nevtum/echopoint.git@master

Getting started
============
#### Create events

Define a new class that contains necessary information about the event that
can later be published by the publisher. The information in each class can be
as much or as little as you like. The events defined in your business domain
will most likely be different to the examples given here.

    class ItemPurchased:
        def __init__(self, item_id, quantity)
            self.id = item_id
            self.qty = quantity

    class ItemReceived:
        pass

#### Subscribe to the event
In this example we subscribe to the ItemPurchased and ItemReceived events
using the decorator in the shortcuts module. Be sure to subscribe to the event
class and not an instance of it. You will receive an error if you do.

    from echopoint.shortcuts import handle

    @handle(ItemPurchased)
    def on_item_purchased(payload):
        id = payload.id
        qty = payload.qty
        # extra execution logic

    @handle(ItemReceived)
    def on_item_received(payload):
        # item received execution logic

Multiple handlers can be subscribed to the same event. A handler can also be
subscribed to a different channel than the default channel.

    @handle(ItemReceived, "debug-channel")
    def handler(payload):
        # execution logic

#### Publish events
Import the publisher from the echopoint.shortcuts module. Events can be
published to the default channel or a custom channel.

    from echopoint.shortcuts import publish

    publish(ItemPurchased('xx-yy-zz', 10))
    publish(ItemReceived())

    # custom channel
    publish(ItemReceived(), "debug-channel")

Please read **shortcut_subscriptions.py** or **messaging.py** in the tests
folder to find a few more samples how Echopoint can be leveraged to subscribe
and publish messages.
