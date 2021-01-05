# module from cmu 15112 class
import module_manager
module_manager.review()

from enemy_class2 import *
from maze_class import *
import time
from player_class import *

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

pygame.init()
pygame.display.set_caption("Into the Maze")

class App(object):         
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.player = Player(self, playerX, playerY)
        self.mazeList = Maze(mazeRow, mazeCol)
        self.maze = self.mazeList.makePath()
        self.enemy = Enemy(self, enemyX, enemyY)
        self.timerDelay = 3000


     
    def run(self):
        #print(self.maze)
        while self.running:
            print 'waiting',self.state
            if self.state == 'start':
                self.button()
                self.start_event()
                self.start_update()
                self.start_draw() 
            elif self.state == 'help':
                self.help_event()
                self.help_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
                self.timerFired()
            elif self.state == 'gameOver':
                self.gameOver_draw()
            elif self.state == 'playerWin':
                self.playerWin_draw()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.state = 'start'
                        self.player.x = 30
                        self.player.y = 30
            else:
                self.running = False
        pygame.quit()
        sys.exit()
        
    
    def draw_text(self, words, screen, pos, size, color, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        pos[0] = pos[0]-text_size[0]//2
        pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)
    
    def reset(self):
        self.player.x = 30
        self.player.y = 30
        self.enemy.row = 1
        self.enemy.col = 11
        #self.getMazeList()
        self.maze = self.mazeList.getRandomPath()
        self.enemy = Enemy(self, enemyX, enemyY)
        #self.reset()
        #print("here")


    def getMazeList(self):
        #self.state = 'start'
        #self.player.x = 30
        #self.player.y = 30

        #pygame.display.update()
        #self.mazeList = Maze(mazeRow, mazeCol)
        self.maze = self.mazeList.getRandomPath()
        self.enemy = Enemy(self, enemyX, enemyY)

        #self.maze = self.mazeList.getRandomPath()

#################################### start #####################################   
    def start_event(self):
        #print("start_event is being called!")
        #print(self.player.x, self.enemy.getEnemyPos(), self.y, self.enemy.getEnemyPos())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
            

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        buttonImg = pygame.transform.scale(pygame.image.load('helpButton.png'), (80,50))
        startImg = pygame.transform.scale(pygame.image.load('helpButton.png'), (220,50))
        self.screen.blit(buttonImg, (60,330))
        self.screen.blit(buttonImg, (250,330)) 
        self.screen.blit(startImg, (80,400))
        
        if 60 < mouse[0] < 140 and 330 < mouse[1] < 380:
            buttonImg = pygame.transform.scale(pygame.image.load('helpButtonFilled.png'), (80,50))
            self.screen.blit(buttonImg, (60,330))
            if click[0] == 1:
                self.state = 'help'

        elif 250 < mouse[0] < 330 and 330 < mouse[1] < 380:
            buttonImg = pygame.transform.scale(pygame.image.load('helpButtonFilled.png'), (80,50))
            self.screen.blit(buttonImg, (250,330))
            if click[0] == 1:
                pygame.quit()
                sys.exit()
        elif 85 < mouse[0] < 305 and 400 < mouse[1] < 450:
            startImg = pygame.transform.scale(pygame.image.load('helpButtonFilled.png'), (220,50))
            self.screen.blit(startImg, (85,400))
            if click[0] == 1:
                self.state = 'playing'
           
        playerImg = pygame.transform.scale(pygame.image.load('player.png'), (100,100))
        self.screen.blit(playerImg, (30,70))
        enemyImg = pygame.transform.scale(pygame.image.load('enemy.png'), (100,100))
        self.screen.blit(enemyImg, (240,75))

        self.draw_text('PRESS SPACE BAR TO START', self.screen, [WIDTH//2, HEIGHT//2],
        START_TEXT_SIZE, (170, 132, 58), START_FONT)
        self.draw_text('WELCOME TO INTO THE MAZE', self.screen, [WIDTH//2, HEIGHT//2-50],
        START_TEXT_SIZE, (200, 100, 100), START_FONT)
        self.draw_text('HELP', self.screen, [100, 345],
        START_TEXT_SIZE1, (255, 255, 255), START_FONT)
        self.draw_text('EXIT', self.screen, [290, 345],
        START_TEXT_SIZE1, (255, 255, 255), START_FONT)
        self.draw_text('S   T   A   R   T', self.screen, [WIDTH//2, 418],
        START_TEXT_SIZE, (255, 255, 255), START_FONT)
        pygame.display.update()
    
    def button(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#################################### help ######################################
    def help_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def help_draw(self):
        self.screen.fill(BLACK)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        helpPageImg = pygame.transform.scale(pygame.image.load('helpPage.png'), (390,570))
        self.screen.blit(helpPageImg, (0,0))

        returnImg = pygame.transform.scale(pygame.image.load('helpButton.png'), (220,50))
        self.screen.blit(returnImg, (85, 450))
        
        if 85 < mouse[0] < 305 and 450 < mouse[1] < 500:
            returnImg = pygame.transform.scale(pygame.image.load('helpButtonFilled.png'), (220,50))
            self.screen.blit(returnImg, (85,450))
            if click[0] == 1:
                self.state = 'start' 
                #print(self.state) 
        self.draw_text('R  E  T  U  R  N', self.screen, [WIDTH//2, 470],
                         START_TEXT_SIZE, BLACK, START_FONT)
        
        pygame.display.update()
    
################################### playing ####################################
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                #self.maze[(self.player.x - 30) // 30][self.player.y // 30]
                if event.key == pygame.K_LEFT and self.player.x-30 >= 0 and self.maze[self.player.y // 30][(self.player.x - 30) // 30] != 1:
                    self.player.x -= 30
                if event.key == pygame.K_RIGHT and self.player.x+60 <= WIDTH and self.maze[self.player.y // 30][(self.player.x + 30) // 30] != 1:
                    self.player.x += 30
                if event.key == pygame.K_UP and self.player.y-30 >= 0 and self.maze[(self.player.y - 30) // 30][self.player.x // 30] != 1:
                    self.player.y -= 30
                if event.key == pygame.K_DOWN and self.player.y+60 <= HEIGHT and self.maze[(self.player.y + 30) // 30][self.player.x // 30] != 1:
                    self.player.y +=30
                if event.key == pygame.K_r:
                    #print("here")
                    self.reset()
                    self.state = 'playing'
                    pygame.display.update()
                    #print(self.state)

    
    
    def timerFired(self):
        if self.enemy.timeToMove():
            time.sleep(0.6)
            #print(f"printing postion: {self.player.x//30, self.y//30}")
            self.enemy.doMove([self.player.x//30, self.player.y//30])
            if self.player.x == self.enemy.getEnemyPos()[0]*30 and self.player.y == self.enemy.getEnemyPos()[1]*30:
                self.state = 'gameOver'
            elif self.maze[self.player.y // 30][self.player.x // 30] == 2:
                self.state = 'playerWin'

    def playing_draw(self):
        self.screen.fill(BLACK)
        wallImg = pygame.transform.scale(pygame.image.load('wall.png'), (29,29))
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 1:
                    self.screen.blit(wallImg, (j*30, i*30))
        pygame.draw.rect(self.screen, (76,187,23), (330, 510, 30, 30))
        
        self.player.draw()
        self.enemy.draw()
        pygame.display.update() 
    
    def playing_update(self):
        pass
                 

################################### game over ##################################

    def gameOver_draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
 
        self.screen.fill(BLACK)
        self.draw_text('GAME OVER!', self.screen, [WIDTH//2, HEIGHT//2-50],
                            GAMEOVER_TEXT_SIZE, (170, 132, 58), START_FONT)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        returnImg = pygame.transform.scale(pygame.image.load('helpButton.png'), (220,50))
        self.screen.blit(returnImg, (85, 450))
        
        if 85 < mouse[0] < 305 and 450 < mouse[1] < 500:
            returnImg = pygame.transform.scale(pygame.image.load('helpButtonFilled.png'), (220,50))
            self.screen.blit(returnImg, (85,450))
            if click[0] == 1:
                self.state = 'start'
                self.reset() 
                #print(self.state) 
        self.draw_text('R  E  T  U  R  N', self.screen, [WIDTH//2, 470],
                         START_TEXT_SIZE, WHITE, START_FONT)
        
        pygame.display.update()
        
################################### you win ###################################       
    def playerWin_draw(self):
        #print(self.maze[self.player.x // 30][self.player.y // 30])
        self.screen.fill(BLACK)
        self.draw_text('YOU WIN!', self.screen, [WIDTH//2, HEIGHT//2-50],
                            GAMEOVER_TEXT_SIZE, (170, 132, 58), START_FONT)
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        returnImg = pygame.transform.scale(pygame.image.load('helpButton.png'), (220,50))
        self.screen.blit(returnImg, (85, 450))
        
        if 85 < mouse[0] < 305 and 450 < mouse[1] < 500:
            returnImg = pygame.transform.scale(pygame.image.load('helpButtonFilled.png'), (220,50))
            self.screen.blit(returnImg, (85, 450))
            if click[0] == 1:
                self.state = 'start' 
                self.reset()
                #print(self.state) 
        self.draw_text('R  E  T  U  R  N', self.screen, [WIDTH//2, 470],
                         START_TEXT_SIZE, WHITE, START_FONT)
        
        pygame.display.update()



