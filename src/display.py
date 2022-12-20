import math
import os
import pygame
import time
from phonemizer import phonemize
from phonemizer.separator import Separator
import random


BLACK = (0, 0, 0)
YELLOW = (247, 187, 51)
SILVER = (53, 57, 58)
WHITE = (255, 255, 255)

ROOT_DIR = os.path.dirname(os.path.abspath(
    __file__))  # This is your Project Root
MOUTH_PATH = os.path.join(ROOT_DIR, "assets/mouths")

# FACE_HAAR = os.path.join(HAAR_PATH, "haarcascade_frontalface_default.xml")

DEFAULT_IMAGE_SIZE = (250, 100)


class Display:

    def __init__(self, screen) -> None:
        self.screen = screen
        self.screen.fill(YELLOW)

        self.pupil_x = 160
        self.pupil_y = 100
        self.x = 160
        self.y = 140

        self.action = "happy"
        self.speak_data = "0001"

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

    def draw_speak_mouth(self, utterance):
        phn = phonemize(
            utterance,
            language='en-us',
            backend='espeak',
            separator=Separator(phone=None, word=' ', syllable='|'),
            strip=True,
            preserve_punctuation=False,
            njobs=4)

        phoneme_list = list(phn)
        print(phoneme_list)
        for i in phoneme_list:
            print("currenty saying : {}".format(i))
            time.sleep(0.1)
            if i == " ":
                self.speak_data = "0009"
            else:
                random_mouth = random.randint(1, 22)
                mouth_txt = f'{random_mouth:04d}'
                print(mouth_txt)
                self.speak_data = mouth_txt
        self.speak_data = "0009"

    def mouth_by_img(self):
        m_img = pygame.image.load(
            os.path.join(MOUTH_PATH, "mouth{}.png".format(self.speak_data)))
        m_img = pygame.transform.scale(m_img, DEFAULT_IMAGE_SIZE)
        self.screen.blit(m_img, (45, 250))

    def draw_mouth(self):
        if (self.action == "happy"):
            m_img = pygame.image.load(
                os.path.join(MOUTH_PATH, "mouth0002.png"))
            m_img = pygame.transform.scale(m_img, DEFAULT_IMAGE_SIZE)

            self.screen.blit(m_img, (45, 250))
        elif (self.action == "sad"):
            pygame.draw.ellipse(self.screen, BLACK, [
                                self.x - 35, 260, 80, 60], 0)
            pygame.draw.ellipse(self.screen, YELLOW, [
                                self.x - 35, 265, 80, 60], 0)
        elif (self.action == "idle"):
            pygame.draw.line(self.screen, BLACK,
                             (140, 260), (180, 260), 10)
        elif (self.action == "speak"):
            self.mouth_by_img()
