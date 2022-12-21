import math
import pygame
import display as d
import face_detection as fd
import json
from threading import Thread


from mycroft_bus_client import MessageBusClient, Message

client = MessageBusClient()
screen = pygame.display.set_mode((320, 480))
display = d.Display(screen)
face_detection = fd.FaceDetection(320, 480)


def main():
    pygame.init()
    done = False
    mycroft_handlers()
    client.run_in_thread()

    while not done:
        display.draw(160, 140)
        faces, region = face_detection.detect()

        display.move_eye_ball(region)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    display.action = "happy"
                    continue
                if event.key == pygame.K_RIGHT:
                    display.action = "sad"
                    continue
            if event.type == pygame.QUIT:
                face_detection.release()
                client.close()
                done = True
        pygame.display.update()


def print_handler(message):
    message_data = json.loads(message.serialize())
    print('Mycroft said "{}"'.format(message_data))


def handle_wake_word(message):
    print('Wake word {}'.format(message.serialize()))
    face_detection.enable_detection = False


def handle_speak(message):
    try:
        message_data = json.loads(message.serialize())
        type = message_data["type"]
        data = message_data["data"]
        print('data - {} - type - {}'.format(data, type))
        face_detection.enable_detection = True

        if data:
            utterance = data["utterance"]
            if utterance:
                display.action = "speak"
                thread = Thread(
                    target=d.Display.draw_speak_mouth, args=[display, utterance])
                thread.start()

            meta = data["meta"]
            print('meta : {}, utterance : {}'.format(meta, utterance))
            if meta:
                skill = meta["skill"]
                meta_data = meta["data"]
                dialog = meta["dialog"]

    except ValueError as excp:
        print('ValueError : {}'.format(excp.msg))
    except KeyError as key_excp:
        print('KeyError : {}'.format(key_excp))
    except RuntimeError as excp:
        print('Runtime Error : {}'.format(excp))


def mycroft_handlers():
    client.on('speak', handle_speak)
    client.on('question:query.response',
              print_handler)
    client.on('mycroft.skill.handler.start',
              print_handler)
    client.on('mycroft.audio.service.play', print_handler)
    client.on('recognizer_loop:wakeword', handle_wake_word)


if __name__ == "__main__":
    main()
