# Written by Yee Shen Teoh

# there is 10 room
# p for porch
# w for lanundry room
# k for kichen
# l for living room
# h for hallway
# d for dining room
# f for foryer
# 1 for bedroom 1
# 2 for bedroom 2
# 3 for bedroom 3

import math
import numpy as np
import random

def best_room(room, start, n, probability, availableRoom):
    for i in range(n):
        probability[i] = 100 - probability[i]
        probability[i] = probability[i]/100
    allQ = []
    for roomName in room:
        if roomName in availableRoom:
            Q = MDP(roomName, n, probability)

            allQ.append(Q)

    # available room will dictate which room is in Q
    start_indx = room.index(start)
    best_state = n+1
    maxQ = 0
    for i in range(len(allQ)):
        for j in range(n):
            if maxQ < allQ[i][start_indx][j]:
                maxQ = allQ[i][start_indx][j]
                best_state = i # the i in availableRoom

    bestPath, totalQ, averageQ = best_path(start, availableRoom[best_state], room, allQ[best_state], n)


    return bestPath

# def best_room(room, start, n, probability, availableRoom):
#     for i in range(n):
#         probability[i] = 100 - probability[i]
#         probability[i] = probability[i]/100

#     highestQ = 0
#     bestPath = []

#     for roomName in room:
#         if roomName in availableRoom:
#             Q = MDP(roomName, n, probability)
#             # print(roomName)
#             # for i in range(10):
#             #     print(Q[i]) 
#             path, totalQ, averageQ = best_path(start, roomName, room, Q, n)

#             if highestQ < averageQ:
#                 highestQ = averageQ
#                 bestPath = path
#     # print(bestPath)
#     # print(highestQ)

#     return bestPath


def best_path(start, end, room, Q, n):
    path = [start]
    start_ind = room.index(start)
    maxQ = 0
    global_maxQ = 0
    curr = start_ind
    next_state = n+1

    totalQ = 0

    if start == end:
        totalQ = Q[curr][curr]
    else:
        while True:
            maxQ = 0
            for i in range(n):
                if maxQ < Q[curr][i]:
                    maxQ = Q[curr][i]
                    next_state = i

            if global_maxQ < maxQ:
                if curr == next_state:
                    break
                totalQ = totalQ + maxQ
                global_maxQ = maxQ
                path.append(room[next_state])
                curr = next_state
            else:
                break

    averageQ = totalQ/len(path)
    # print(path)
    # print(averageQ)
    # print(totalQ)
    return path, totalQ, averageQ

# find utility from one room to all other room, and then check which one have the highest reward
def MDP(end, n, probability):
    Q = [[0]*n for _ in range(n)]
    discound = 0.8
    epsilon = 0.0001
    checker = 0
    reward = make_reward(end, n)
    while checker < 100:
        changes = total_Q(Q)
        Q = Qlearning(discound, reward, Q, n, probability)
        changes = total_Q(Q) - changes
        if changes < 0:
            changes = changes*-1
        if changes < epsilon:
            checker = checker + 1
        else:
            checker = 0
    for i in range(10):
        for j in range(10):
            Q[i][j] = round(Q[i][j])
    return Q


def total_Q(Q):
    totalQ = 0
    for i in range(10):
        for j in range(10):
            totalQ = totalQ+ Q[i][j]
    return totalQ

def Qlearning(discound, reward, Q, n, probability):
    tempQ = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if reward[i][j] != -1:
                tempQ[i][j] = (reward[i][j] + discound*next_maxQ(Q,j))*probability[j]
    return tempQ


def next_maxQ(Q, next_state):
    maxQ = 0
    for i in range(10):
        if Q[next_state][i] >= maxQ:
            maxQ = Q[next_state][i]
    return maxQ 

def make_reward(end, n):
    reward = [[-1]*n for _ in range(n)]
    for i in range(n):
        reward[i][i] = 0
    reward[0][1] = 0
    reward[1][0] = 0
    reward[0][3] = 0
    reward[3][0] = 0
    reward[1][2] = 0
    reward[2][1] = 0
    reward[1][4] = 0
    reward[4][1] = 0
    reward[2][5] = 0
    reward[5][2] = 0
    reward[3][4] = 0
    reward[4][3] = 0
    reward[4][6] = 0
    reward[6][4] = 0
    reward[4][7] = 0
    reward[7][4] = 0
    reward[4][8] = 0
    reward[8][4] = 0
    reward[4][9] = 0
    reward[9][4] = 0
    reward[5][6] = 0
    reward[6][5] = 0

    num = 1000
    selfRew = num*1.1
    if end == 'p':
        reward[0][0] = selfRew
        reward[1][0] = num
        reward[3][0] = num
    elif end == 'w':
        reward[1][1] = selfRew
        reward[0][1] = num
        reward[2][1] = num
        reward[4][1] = num
    elif end == 'k':
        reward[2][2] = selfRew
        reward[1][2] = num
        reward[5][2] = num
    elif end == 'l':
        reward[3][3] = selfRew
        reward[0][3] = num
        reward[4][3] = num
    elif end == 'h':
        reward[4][4] = selfRew
        reward[1][4] = num
        reward[3][4] = num
        reward[6][4] = num
        reward[7][4] = num
        reward[8][4] = num
        reward[9][4] = num
    elif end == 'd':
        reward[5][5] = selfRew
        reward[2][5] = num
        reward[6][5] = num
    elif end == 'f':
        reward[6][6] = selfRew
        reward[4][6] = num
        reward[5][6] = num
    elif end == '1':
        reward[7][7] = selfRew
        reward[4][7] = num
    elif end == '2':
        reward[8][8] = selfRew
        reward[4][8] = num
    elif end == '3':
        reward[9][9] = selfRew
        reward[4][9] = num

    return reward