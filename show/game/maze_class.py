# module from cmu 15112 class
# maze generation algorithm from Randomized Prim's algorithm
# https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Prim's_algorithm

import module_manager
module_manager.review()

import random
from settings import *


class Maze(object):
    def __init__(self, mazeRow, mazeCol):
        self.row = mazeRow
        self.col = mazeCol
        self.emptyRoomFlag = True
        self.mazeList = mazeList1#copy.deepcopy(mazeList1)
  
    def getCell(self,i,j):
        return self.mazeList[i][j]

    def setCell(self,i,j,value = None):
        self.mazeList[i][j] = value

    def checkCell(self, i1, j1, i2, j2, i3, j3):
        if self.getCell(i1,j1) == 1:
            if self.getCell(i2, j2) == 2:
                if self.getCell(i3, j3) == 0:
                    self.setCell(i1,j1, value = 0)
                    self.setCell(i2,j2, value = 0)
                    self.setCell(i3,j3, value = 0)

# the main algorithm for maze generation and original source code
# from http://gsw7.net/K700003.php
    
    def makePath(self):
        while self.emptyRoomFlag:
            self.emptyRoomFlag = False
            for x in range(1, 18):
                for y in range(1, 12):
                    #print(x,y)
                    R = random.randint(1,5)
                    #random.seed(R)
                    if R == 1:
                        self.checkCell(x, y, x+1, y, x-1, y)
                    if R == 2:
                        self.checkCell(x, y, x-1, y, x+1, y)
                    if R == 3:
                        self.checkCell(x, y, x, y+1, x, y-1)
                    if R == 4:
                        self.checkCell(x, y, x, y-1, x, y+1)
                    if self.getCell(x, y) == 2:
                        self.emptyRoomFlag = True
        self.mazeList[17][11] = 2
        return self.mazeList
    def getRandomPath(self):
        self.emptyRoomFlag = True
        self.mazeList = mazeList1 #copy.deepcopy(mazeList1)
        return self.makePath()

    



    
