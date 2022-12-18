import math
import pygame
import display as d
import face_detection as fd


screen = pygame.display.set_mode((320, 480))
display = d.Display(screen)
face_detection = fd.FaceDetection(320, 480)


def main():
    pygame.init()
    done = False
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
                done = True
        pygame.display.update()


if __name__ == "__main__":
    main()
