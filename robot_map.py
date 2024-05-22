# Written by Yee Shen Teoh

import math
import numpy as py

class Map:
    def __init__(self, mapDimension, obstacle):
        self.mapDimension = mapDimension
        self.map = []
        self.obstacle = obstacle

        self.createMap()
        self.createObs()
        self.roomSetup()
        # self.robot_pos((29, 16))
        # self.robot_pos((14,16))
        # self.robot_pos((25, 16))
        # self.robot_pos((31,18))
        # self.robot_pos((43, 14))
        # self.robot_pos((45, 18))
        # self.robot_pos((49, 18))
        # self.robot_pos((12, 9))
        # self.robot_pos((14, 1))
        # self.robot_pos((12, 18))
        # self.robot_pos((14, 31))
        # self.robot_pos((29, 31))

    def recreateMap(self):
        self.map = []
        self.createMap()
        self.createObs()
        self.roomSetup()

    def createMap(self):
        mapW, mapH = self.mapDimension
        grid = []
        for width in range(mapW):
            grid.append('+')
        temp = grid.copy()
        for height in range(mapH):
            self.map.append(temp.copy())

    def robot_pos(self, curr):
        robotW, robotH = curr
        self.map[robotH][robotW] = 'R'
        self.map[robotH+1][robotW] = 'R'
        self.map[robotH][robotW+1] = 'R'
        self.map[robotH+1][robotW+1] = 'R'


    def printMap(self):
        mapW, mapH = self.mapDimension
        for height in range(mapH):
            for width in range(mapW-1):
                print(self.map[height][width], end="")
            print(self.map[height][mapW-1])

    def putObj(self, corA, corB, char):
        widthA, heightA = corA
        widthB, heightB = corB
        width = widthB-widthA
        height = heightB-heightA
        for i in range (height):
            for j in range(width):
                self.map[heightA + i][widthA+j] = char

    def createObs(self):
        for obstacle in self.obstacle:
            self.putObj(obstacle[0], obstacle[1], '0')

    def roomSetup(self):
        # #porch
        self.putObj((1,1),(14,9),'p')
        #washroom
        self.putObj((1,11),(14,18),'w')
        #kitchen
        self.putObj((1,20),(14,33),'k')
        #living room
        self.putObj((16,1),(35,16),'l')
        #hallway
        self.putObj((16,16),(53,18),'h')
        #dining
        self.putObj((16,20),(29,33),'d')
        #Foyer
        self.putObj((31,20),(35,33),'f')
        #bedroom 1
        self.putObj((43,1),(53,14),'1')
        #bedroom 2
        self.putObj((37,20),(47,33),'2')
        #bedroom 3
        self.putObj((49,20),(59,33),'3')
        pass

def MemToRoom(cor):
    x, y = cor

    if x >= 1 and x < 14 and y >= 1 and y < 9:
        room = 'p'
    elif x >= 1 and x < 14 and y >= 11 and y < 18:
        room = 'w'
    elif x >= 1 and x < 14 and y >= 20 and y < 33:
        room = 'k'
    elif x >= 16 and x < 35 and y >= 1 and y < 16:
        room = 'l'
    elif x >= 16 and x < 53 and y >= 16 and y < 18:
        room = 'h'
    elif x >= 16 and x < 29 and y >= 20 and y < 33:
        room = 'd'
    elif x >= 31 and x < 35 and y >= 20 and y < 33:
        room = 'f'
    elif x >= 43 and x < 53 and y >= 1 and y < 14:
        room = '1'
    elif x >= 37 and x < 47 and y >= 20 and y < 33:
        room = '2'
    elif x >= 49 and x < 59 and y >= 20 and y < 33:
        room = '3'
    else:
        room = '+'

    return room


def roomToMem(room):
    corx = 0
    cory = 0

    if room == 'p':
        corx = 3
        cory = 3
    elif room == 'w':
        corx = 7
        cory = 13
    elif room == 'k':
        corx = 7
        cory = 28
    elif room == 'l':
        corx = 23
        cory = 8
    elif room == 'h':
        corx = 40
        cory = 16
    elif room == 'd':
        corx = 23
        cory = 27
    elif room == 'f':
        corx = 32
        cory = 25
    elif room == '1':
        corx = 47
        cory = 7
    elif room == '2':
        corx = 42
        cory = 27
    elif room == '3':
        corx = 53
        cory = 27

    return (corx, cory)


def converMemToSim(cor):
    memX, memY = cor
    simY = memY - 16
    simX = -1*(memX - 29)
    return (simX*.1, simY*.1)

def start():
    obstacle = []
    # first is width, second is height
    obs1 = ((0,0),(60, 1))
    obs2 = ((0,0),(1, 34))
    obs3 = ((59,0),(60, 34))
    obs4 = ((0,33),(60, 34))

    obs5 = ((1,9),(12, 11))
    obs6 = ((14, 3),(16, 16))
    obs7 = ((1, 18),(12, 20))
    obs8 = ((14, 18),(16, 31))

    obs9 = ((14, 18),(31, 20))
    obs10 = ((29,18),(31,31))

    obs11 = ((33, 18),(45, 20))
    obs12 = ((35, 18),(37, 34))
    obs13 = ((47, 18),(49,34))
    obs14 = ((51, 18),(60, 20))

    obs15 = ((35, 1),(43, 16))
    obs16 = ((45, 14),(54, 16))
    obs17 = ((53, 1),(60, 19))

    obstacle.append(obs1)
    obstacle.append(obs2)
    obstacle.append(obs3)
    obstacle.append(obs4)
    obstacle.append(obs5)
    obstacle.append(obs6)
    obstacle.append(obs7)
    obstacle.append(obs8)
    obstacle.append(obs9)
    obstacle.append(obs10)
    obstacle.append(obs11)
    obstacle.append(obs12)
    obstacle.append(obs13)
    obstacle.append(obs14)
    obstacle.append(obs15)
    obstacle.append(obs16)
    obstacle.append(obs17)

    temp = Map((60, 34), obstacle)

    return temp