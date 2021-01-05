# module from 15112 class
# path finding algorithm inspired by A Plus Coding from youtube
# https://www.youtube.com/playlist?list=PLryDJVmh-ww3AMl8NSjp9YygWWTOfePu7
import module_manager
module_manager.review()

import pygame
from app_class import *

UP = [0,-1]
DOWN = [0,1]
RIGHT = [1,0]
LEFT = [-1,0]

# enemyImg from google
enemyImg = pygame.transform.scale(pygame.image.load('enemy.png'), (30,30))

class Enemy(object):
    def __init__(self, app, enemyX, enemyY):
        self.app = app
        self.x = enemyX
        self.y = enemyY
        self.maze = self.app.maze
        self.col = self.x //30
        self.row = self.y //30
        
    def timeToMove(self):
        if not (self.app.player.x == 30 and self.app.player.y == 30):
            return True
        return False

    def doMove(self, target):
        path = self.findPath([self.col, self.row], target)
        if len(path) >= 2:
            nextPos = path[1]
            self.col = nextPos[0]
            self.row = nextPos[1]
        else:
            return None

    def getEnemyPos(self):
        #print(self.row)
        #print(f"getEnemyPos {self.row, self.col}")
        return [self.col, self.row]
        
    def findPath(self, start, target):
        grid = self.maze
        queue = [start]
        path = []
        visited = []
        while queue:
            current = queue[0]
            queue.remove(queue[0])
            visited.append(current)
            if current == target:
                break
            else:
                neighbours = [UP, DOWN, RIGHT, LEFT]
                for neighbour in neighbours:
                    if 0 <= neighbour[0]+current[0] < len(grid[0]):
                        if 0 <= neighbour[1]+current[1] < len(grid):
                            next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
                            if next_cell not in visited:
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    queue.append(next_cell)
                                    path.append({"Current": current, "Next": next_cell})
        shortest = [target]
        while target != start:
            for step in path:
                if step["Next"] == target:
                    target = step["Current"]
                    shortest.insert(0, step["Current"])
        #print(shortest)
        return shortest

    def draw(self):
        #pygame.draw.rect(self.app.screen, enemyColor, (self.row*30, self.col*30, 30, 30))
        self.app.screen.blit(enemyImg, (self.col*30, self.row*30))
        #print(self.row, self.col)
