import math
import pygame
import display as d
import face_detection as fd
import mycroft_bus as my

from mycroft_bus_client import MessageBusClient, Message

client = MessageBusClient()
screen = pygame.display.set_mode((320, 480))
display = d.Display(screen)
face_detection = fd.FaceDetection(320, 480)
mycroft_handle = my.MycroftHandler()


def main():
    pygame.init()
    done = False
    mycroft_handlers()
    client.run_forever()

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


def mycroft_handlers():
    client.on('speak', mycroft_handle.handle_speak)
    client.on('question:query.response',
              mycroft_handle.handle_question_response)
    client.on('mycroft.audio.service.play', mycroft_handle.handle_audio_play)


if __name__ == "__main__":
    main()
