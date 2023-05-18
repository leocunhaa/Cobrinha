import pygame
import random
from pygame.locals import *

screen = pygame.display.set_mode((700,700))

def gridRandom():
    x = random.randint(0,55)
    y = random.randint(0,55)
    return (x * 10, y * 10)

def collision(c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def text():
    txt = "GAME OVER"
    pygame.font.init()
    fonte = pygame.font.get_default_font()
    fontesys = pygame.font.SysFont(fonte, 60)
    txttela = fontesys.render(txt, 1, (255,255,255))
    screen.blit(txttela, (225,280))
    pygame.display.update()
