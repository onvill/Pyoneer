#!/usr/bin/env python

import pygame, sys, time, random
from pygame.locals import *

class SnakeTest():
    def __init__(self,tmp = []):
        pygame.init()

        self.fpsClock = pygame.time.Clock()

        self.playSurface = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Raspberry Snake')

        # Create Grid
        self.WINDOWWIDTH = 640
        self.WINDOWHEIGHT = 480
        self.CELLSIZE = 20
        self.DARKGRAY  = ( 40,  40,  40)

        # Create Colours
        self.redColour = pygame.Color(255, 0, 0)
        self.blackColour = pygame.Color(0, 0, 0)
        self.whiteColour = pygame.Color(255, 255, 255)
        self.greyColour = pygame.Color(150, 150, 150)
        self.greenColour = pygame.Color(0,255,0)

        #Create snake Position
        self.snakePosition = [100,100]
        self.snakeSegments = [[100,100],[80,100],[60,100]]

        #Create Raspberry Position
        self.raspberryPosition = [0,0]
        self.raspberrySpawned = 1

        self.direction = 'right'
        self.changeDirection = self.direction
        # Converte String if Moves into moves
        self.listMoves = tmp
        self.count  = 0
        self.runGame()
    # Draw Grid
    def drawGrid(self):
        for x in range(0, self.WINDOWWIDTH, self.CELLSIZE): # draw vertical lines
            pygame.draw.line(self.playSurface, self.DARKGRAY, (x, 0), (x, self.WINDOWHEIGHT))
        for y in range(0, self.WINDOWHEIGHT, self.CELLSIZE): # draw horizontal lines
            pygame.draw.line(self.playSurface, self.DARKGRAY, (0, y), (self.WINDOWWIDTH, y))
            
    # Function when user looses
    def gameOver(self):
        print "entered gameover method"
        gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
        gameOverSurf = gameOverFont.render('Game Over', True, self.redColour)
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.midtop = (320, 10)
        self.playSurface.blit(gameOverSurf, gameOverRect)
        pygame.display.update()
        print "just about to pygame quite \n"
        pygame.quit()
        print "pygame quite \n"
        sys.exit()
        
    # Ceate set of obstacles    
    def createObstacle(self):
        for x in range(0,400,self.CELLSIZE):
            pygame.draw.rect(self.playSurface,self.greenColour,(x,20,20,20))
        for x in range(20,400,self.CELLSIZE):
            pygame.draw.rect(self.playSurface,self.greenColour,(400,x,20,20))
        for x in range(440,640,self.CELLSIZE):
            pygame.draw.rect(self.playSurface,self.greenColour,(x,20,20,20))
        for x in range(20,400,self.CELLSIZE):
            pygame.draw.rect(self.playSurface,self.greenColour,(440,x,20,20))

    # Function when user completes the level
    def levelCompleted(self):
        levelCompletedFont = pygame.font.Font('freesansbold.ttf', 72)
        levelCompletedSurf = levelCompletedFont.render('Level Completed', True, greenColour)
        levelCompletedRect = levelCompletedSurf.get_rect()
        levelCompletedRect.midtop = (320, 10)
        self.playSurface.blit(levelCompletedSurf, levelCompletedRect)
        pygame.display.flip()
        pygame.quit()
        sys.exit()
    # chech if user hits the obstacle    
    def checkObstacle(self):
        for x in range(0,400,self.CELLSIZE):
            if self.snakePosition[0] == x and self.snakePosition[1]==20:
                self.gameOver()
            else:
                pass
        for x in range(20,400,self.CELLSIZE):
            if self.snakePosition[0] == 400 and self.snakePosition[1]==x:
                self.gameOver()
            else:
                pass
        for x in range(440,640,self.CELLSIZE):
            if self.snakePosition[0] == x and self.snakePosition[1]==20:
                self.gameOver()
            else:
                pass
        for x in range(20,400,self.CELLSIZE):
            if self.snakePosition[0] == 440 and self.snakePosition[1]==x:
                self.gameOver()
            else:
                pass
    def runGame(self):
        for move in self.listMoves: 
            if move == "moveRight()":
                self.changeDirection = 'right'
                if self.changeDirection == 'right' and not self.direction == 'left':
                    self.direction = self.changeDirection
                if self.direction == 'right':
                    self.snakePosition[0] += 20
                    self.count = self.count + 1
                    print move
            if move == "moveLeft()": 
                self.changeDirection = 'left'
                if self.changeDirection == 'left' and not self.direction == 'right':
                    self.direction = self.changeDirection
                if self.direction == 'left':
                    self.snakePosition[0] -= 20
                    print move
            if move == "moveUp()":
                self.changeDirection = 'up'
                if self.changeDirection == 'up' and not self.direction == 'down':
                    self.direction = self.changeDirection
                if self.direction == 'up':
                    self.snakePosition[1] -= 20
                    print move
            if move == "moveDown()": 
                self.changeDirection = 'down'
                if self.changeDirection == 'down' and not self.direction == 'up':
                    self.direction = self.changeDirection
                if self.direction == 'down':
                    self.snakePosition[1] += 20
                    print move
                
            self.snakeSegments.insert(0,list(self.snakePosition))
            if self.snakePosition[0] == self.raspberryPosition[0] and self.snakePosition[1] == self.raspberryPosition[1]:
                self.raspberrySpawned = 0
                self.levelCompleted()
            else:
                self.snakeSegments.pop()
            if self.raspberrySpawned == 0:
                x = random.randrange(1,32)
                y = random.randrange(1,24)
                raspberryPosition = [int(x*20),int(y*20)]
            raspberrySpawned = 1
            
            self.playSurface.fill(self.blackColour)
            self.drawGrid()
            self.createObstacle()
            self.checkObstacle()
            
            for position in self.snakeSegments:
                pygame.draw.rect(self.playSurface,self.whiteColour,Rect(position[0], position[1], 20, 20))
                pygame.draw.rect(self.playSurface,self.redColour,Rect(self.raspberryPosition[0], self.raspberryPosition[1], 20, 20))
            pygame.display.flip()

            time.sleep(1)
            if self.snakePosition[0] > 620 or self.snakePosition[0] < 0:
                self.gameOver()
            if self.snakePosition[1] > 460 or self.snakePosition[1] < 0:
                self.gameOver()
            if self.count == len(self.listMoves)-1:
                self.gameOver()
            self.fpsClock.tick(1)
