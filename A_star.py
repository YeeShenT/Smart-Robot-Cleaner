# Written by Yee Shen Teoh

import heapq
from robot import *
import math
import numpy as np

class PathPlanning:
    def __init__(self, position, parent):
        self.position = position
        self.x, self.y = position
        self.parent = parent
        self.parent_x, self.parent_y = parent
        self.gCost = 0
        self.hCost = 0


    def DistanceToPoint(self, cordinate):
        corX, corY = cordinate
        return math.sqrt((corX - self.x)**2 + (corY - self.y)**2)

    def Cost(self, goal, preCor, parentGCOst):
        gCost = parentGCOst
        distanceToPre = self.DistanceToPoint(preCor)
        distanceToGoal = self.DistanceToPoint(goal)
        self.gCost = round(gCost + distanceToPre*100)
        self.hCost = round(distanceToGoal*100)

    def Action(self):
        action = []
        # there should be 8 action, for each direction
        x, y = self.position
        for i in range(3):
            temp_x = x + i - 1
            for j in range(3):
                temp_y = y + j - 1
                if not(temp_x == x and temp_y == y):
                    temp = [temp_x, temp_y]
                    action.append(temp.copy())
        return action

def checkRightRoom(position, Map, roomAllowed):
    posX, posY = position
    # Room allowed will have pwklhdf123
    isAllow = False
    for room in roomAllowed:
        if Map.map[posY][posX] == room:
            isAllow = True

    return isAllow
        
def checkBlocked(position, Map): #Need to modify since robot are big
    #robot size is one unit to the right and bottom
    posX, posY = position
    mapX, mapY = Map.mapDimension
    if posX < 0 or posY < 0 or posX+1 >= mapX or posY+1 >= mapY:
        return True
    
    if(Map.map[posY][posX] == '0') or (Map.map[posY+1][posX] == '0') or (Map.map[posY][posX+1] == '0') or (Map.map[posY+1][posX+1] == '0'):
        return True
    return False

def PrintPath(state, closedState, map, start,savePath):
    if(state.parent == start):
        tempX, tempY = state.position
        # map.map[tempY][tempX] = 'r'
        savePath.append((tempX, tempY))
        return
    if state.parent in closedState:
        PrintPath(closedState[state.parent], closedState, map, start,savePath)
        tempX, tempY = state.position
        # map.map[tempY][tempX] = 'r'
        savePath.append((tempX, tempY))
        return
    

def AStar(start, goal, map, roomAllowed):
    closedState = {}
    openState = []
    openState_helper = {}

    FirstState = PathPlanning(start, start)
    FirstState.Cost(goal, start, 0)
    heapq.heappush(openState, (FirstState.gCost + FirstState.hCost, FirstState.gCost, FirstState.position))
    openState_helper[FirstState.position] = (FirstState.gCost, FirstState.hCost, FirstState)
    
    while(len(openState)>0):
        cost, gCost, curPosition = heapq.heappop(openState)
        if curPosition in openState_helper:
            gCost, hCost, curState = openState_helper.pop(curPosition)

            if curState.position == goal:
                break

            closedState[curState.position] = curState
            actionList = curState.Action()

            for action in actionList:
                actx, acty = action
                if (not (actx,acty) in closedState) and (not checkBlocked(action, map)) and checkRightRoom(action, map, roomAllowed):
                    parentGCost = curState.gCost
                    tempState = PathPlanning((actx, acty), curState.position)
                    tempState.Cost(goal, curState.position, parentGCost)

                    if (actx, acty) in openState_helper:
                        gCost_open, hCost_open, openClass = openState_helper[(actx, acty)]
                        if (gCost_open + hCost_open)>(tempState.gCost + tempState.hCost):
                            openState_helper.pop(tempState.position)
                            openState_helper[tempState.position] = (tempState.gCost, tempState.hCost, tempState)
                            heapq.heappush(openState, (tempState.gCost + tempState.hCost, tempState.gCost, tempState.position))
                        elif (gCost_open + hCost_open) == (tempState.gCost+tempState.hCost):
                            if gCost_open > tempState.gCost:
                                openState_helper.pop(tempState.position)
                                openState_helper[tempState.position] = (tempState.gCost, tempState.hCost, tempState)
                                heapq.heappush(openState, (tempState.gCost + tempState.hCost, tempState.gCost, tempState.position))
                    else:
                        openState_helper[tempState.position] = (tempState.gCost, tempState.hCost, tempState)
                        heapq.heappush(openState, (tempState.gCost + tempState.hCost, tempState.gCost, tempState.position))
    savePath = [start]
    PrintPath(curState, closedState, map, start, savePath)
    # map.printMap()

    # print(savePath)

    return savePath



# Test

# map = robot_mem()
# map.printMap()

# AStar(start, goal, map, roomAllowed)