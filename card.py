import time

from pygame.locals import *
import pygame
import numpy as np


EMPTY = (230, 230, 230)
LOOKED = (200,200,200)
GRAY = (150, 150, 150)

class card:
    def __init__(self,x,y,a="0"):
        self.content=a
        self.x=x
        self.y=y
        self.state = 0


    def turn(self):
        self.state = 1

    def hide(self):
        self.state = 2

    def turnback(self):
        self.state = 0

    def check_click(self,x,y):
        if (self.x<x<self.x+180) and (self.y<y<self.y+180):
            if self.state == 0:
                self.turn()
                return True
            else:
                return False

    def display(self,screen,font):
        rect = Rect(self.x, self.y, 180, 180)
        if self.state == 0:
            pygame.draw.rect(screen, EMPTY, rect)

        elif self.state == 1:
            pygame.draw.rect(screen, LOOKED, rect)
            text = font.render(self.content, True, (0, 0, 0), (LOOKED))
            screen.blit(text, (self.x+80, self.y+80))
        else:
            pygame.draw.rect(screen, GRAY, rect)


