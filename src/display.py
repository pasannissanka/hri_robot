import math
import pygame


BLACK = (0, 0, 0)
YELLOW = (247, 187, 51)
SILVER = (53, 57, 58)
WHITE = (255, 255, 255)


class Display:

    def __init__(self, screen) -> None:
        self.screen = screen
        self.screen.fill(YELLOW)

        self.pupil_x = 160
        self.pupil_y = 100
        self.x = 160
        self.y = 140

        self.action = "happy"

    def draw(self, x, y):
        self.screen.fill(YELLOW)

        self.x = x
        self.y = y

        self.draw_eye()
        self.draw_mouth()

    def draw_eye(self):
        # Belt
        pygame.draw.rect(self.screen, BLACK, [0, 110, 320, 60], 0)
        # Glasses
        pygame.draw.circle(self.screen, SILVER, (self.x, self.y), 90)
        # Eye
        pygame.draw.circle(self.screen, WHITE, (self.x, self.y), 70)
        # Pupil
        pygame.draw.circle(
            self.screen, BLACK, (self.pupil_x, self.pupil_y), 25)

    def move_eye_ball(self, region):
        region_x = region[0]
        region_y = region[1]

        if region_x == 1 and region_y == 1:
            self.pupil_x = 138.9
            self.pupil_y = 116.9
        elif region_x == 1 and region_y == 2:
            self.pupil_x = 129.9
            self.pupil_y = 137.9
        elif region_x == 1 and region_y == 3:
            self.pupil_x = 140.9
            self.pupil_y = 162.9
        elif region_x == 2 and region_y == 1:
            self.pupil_x = 157.9
            self.pupil_y = 119.9
        elif region_x == 2 and region_y == 2:
            self.pupil_x = self.x
            self.pupil_y = self.y
        elif region_x == 2 and region_y == 3:
            self.pupil_x = 161.9
            self.pupil_y = 168.9
        elif region_x == 3 and region_y == 1:
            self.pupil_x = 179.9
            self.pupil_y = 117.9
        elif region_x == 3 and region_y == 2:
            self.pupil_x = 188.9
            self.pupil_y = 138.9
        elif region_x == 3 and region_y == 3:
            self.pupil_x = 178.9
            self.pupil_y = 161.9
        elif region_x == 0 and region_y == 0:
            self.pupil_x = self.x
            self.pupil_y = self.y

    def draw_mouth(self):
        if (self.action == "happy"):
            pygame.draw.ellipse(self.screen, BLACK, [
                                self.x - 35, 240, 80, 60], 0)
            pygame.draw.ellipse(self.screen, YELLOW, [
                                self.x - 35, 235, 80, 60], 0)
        elif (self.action == "sad"):
            pygame.draw.ellipse(self.screen, BLACK, [
                                self.x - 35, 260, 80, 60], 0)
            pygame.draw.ellipse(self.screen, YELLOW, [
                                self.x - 35, 265, 80, 60], 0)
