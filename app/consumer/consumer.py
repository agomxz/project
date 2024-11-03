from app.contexts.shared.infrastructure.rabbit_event_bus import RabbitmqConsumer
from app.consumer.user_controller import user_controller


services = [
    {
        "exchange": "user.domain_events",
        "routing_key": "carrier.carrier.disable",
        "queue": "user.disable_access_on_carrier_disabled",
        "service": user_controller,
    },
    {
        "exchange": "user.domain_events",
        "routing_key": "client.client.disable",
        "queue": "user.disable_access_on_client_disabled",
        "service": user_controller,
    },
]


def consume():
    consumer = RabbitmqConsumer(name="UsersConsumer")
    consumer.set_services(services)

    try:
        consumer.start()
    except KeyboardInterrupt:
        consumer.stop()


def declare_queues():
    rabbitmq_consumer = RabbitmqConsumer()

    for service in services:
        RabbitmqConsumer.declare_queue(
            exchange=service["exchange"],
            routing_key=service["routing_key"],
            queue=service["queue"],
            channel=rabbitmq_consumer.channel,
        )
