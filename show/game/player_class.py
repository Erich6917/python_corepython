# module from 15112 class
import module_manager
module_manager.review()

import pygame

# playerImge from google 
# https://dlpng.com/png/6489026
playerImg = pygame.transform.scale(pygame.image.load('player.png'), (30,30))
class Player(object):
    def __init__(self, app, playerX, playerY):
        self.app = app
        self.x = playerX
        self.y = playerY
        self.validMove = True
    
    def draw(self):
        #pygame.draw.rect(self.app.screen, playerColor, (self.x, self.y, 30, 30))
        self.app.screen.blit(playerImg, (self.x, self.y))