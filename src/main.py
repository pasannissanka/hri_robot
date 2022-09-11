import math
import pygame


def draw():
    def draw_eye(eye_x, eye_y):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        distance_x = mouse_x - eye_x
        distance_y = mouse_y - eye_y
        distance = min(math.sqrt(distance_x**2 + distance_y**2), 30)
        angle = math.atan2(distance_y, distance_x)

        pupil_x = eye_x + (math.cos(angle) * distance)
        pupil_y = eye_y + (math.sin(angle) * distance)

        pygame.draw.circle(screen, (255, 255, 255), (eye_x, eye_y), 50)
        pygame.draw.circle(screen, (0, 0, 100), (pupil_x, pupil_y), 15)
    draw_eye(110, 100)
    draw_eye(220, 100)


def main():
    pygame.init()
    done = False
    while not done:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.update()


if __name__ == "__main__":
    screen = pygame.display.set_mode((320, 480))
    main()
