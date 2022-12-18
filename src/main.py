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

        faces = face_detection.detect()
        # print(faces)

        x = display.x
        y = display.y
        mouse_x, mouse_y = pygame.mouse.get_pos()

        distance_x = mouse_x - x
        distance_y = mouse_y - y
        distance = min(math.sqrt(distance_x**2 + distance_y**2), 30)
        angle = math.atan2(distance_y, distance_x)

        pupil_x = x + (math.cos(angle) * distance)
        pupil_y = y + (math.sin(angle) * distance)

        display.pupil_x = pupil_x
        display.pupil_y = pupil_y

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
