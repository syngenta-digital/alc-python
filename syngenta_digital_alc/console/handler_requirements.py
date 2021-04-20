from syngenta_digital_alc.console.event_client import EventClient


def handler_requirements():
    def decorator_func(func):
        def wrapper(event, context):
            client = EventClient(event, context)
            func(client)
        return wrapper
    return decorator_func