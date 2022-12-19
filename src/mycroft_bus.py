# from mycroft_bus_client import MessageBusClient, Message

# print('Setting up client to connect to a local mycroft instance')
# client = MessageBusClient()


# def print_utterance(message):
#     print('Mycroft said "{}"'.format(message.data.get('utterance')))


# def print_handler(message):
#     print('Mycroft said "{}"'.format(message.serialize()))


# print('Registering handler for speak message...')
# client.on('speak', print_utterance)


# print('Registering handler for question:query.response')
# client.on('question:query.response', print_handler)

# print('Registering handler for mycroft.audio.service.play')
# client.on('mycroft.audio.service.play', print_handler)

# client.run_forever()


# class MycroftBus:
#     def __init__(self) -> None:
#         pass
