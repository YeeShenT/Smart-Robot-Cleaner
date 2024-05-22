# Written by Yee Shen Teoh

import heapq
from robot import *
import math
import numpy as np
from A_star import *

# Cleaned Path
def clean_room(room):
    start_h = 0
    start_w = 0
    height = 0
    width = 0
    if room == 'p': # porch ((1,1),(14,9),'p')
        start_w = 1
        start_h = 1
        width = 13
        height = 8
    elif room == 'w': # washroom ((1,11),(14,18),'w')
        start_w = 1
        start_h = 11
        width = 13
        height = 17
    elif room == 'k': # kitchen ((1,20),(14,33),'k')
        start_w = 1
        start_h = 20
        width = 13
        height = 32
    elif room == 'l': # living room ((16,1),(35,16),'l')
        start_w = 16
        start_h = 1
        width = 34
        height = 15
    elif room == 'h': # hallway ((16,16),(53,18),'h')
        start_w = 16
        start_h = 16
        width = 52
        height = 17
    elif room == 'd': # dining ((16,20),(29,33),'d')
        start_w = 16
        start_h = 20
        width = 28
        height = 32
    elif room == 'f': # Foyer ((31,20),(35,33),'f')
        start_w = 31
        start_h = 20
        width = 34
        height = 32
    elif room == '1': # bedroom 1 ((43,1),(53,14),'1')
        start_w = 43
        start_h = 1
        width = 52
        height = 13
    elif room == '2': # bedroom 2 ((37,20),(47,33),'2')
        start_w = 37
        start_h = 20
        width = 46
        height = 32
    elif room == '3': # bedroom 3 ((49,20),(59,33),'3')
        start_w = 49
        start_h = 20
        width = 58
        height = 32 

    start = (start_w, start_h)
    savePath = [start]

    w = start_w
    h = start_h

    maxW = width
    maxH = height
    forward = True



    while h < maxH:
        while w < maxW and w >= start_w:
            if forward:
                if w == maxW-1:
                    break
                else:
                    w = w+1
            elif not forward:
                if w == start_w:
                    break
                else:
                    w = w-1
            
            savePath.append((w,h))
        forward = not forward

        if h == maxH - 1:
            break

        if h + 2 >= maxH-1:
            h = h+1
            savePath.append((w,h))
        else:
            h = h+1
            savePath.append((w,h))
            h = h+1
            savePath.append((w,h))

        savePath.append((w,h))

    return savePath


def to_door(roomAllowed):
    temp = roomAllowed.copy()
    # get the last 2
    last = temp.pop()
    second_last = temp.pop()
    if last == '+':
        last = second_last
        second_last = temp.pop()

    if last == 'p':
        if second_last == 'w':
            corx = 12
            cory = 9
        elif second_last == 'l':
            corx = 14
            cory = 1
        else:
            corx = 13
            cory = 5

    elif last == 'w':
        if second_last == 'p':
            corx = 12
            cory = 9
        elif second_last == 'h':
            corx = 14
            cory = 16
        elif second_last == 'k':
            corx = 12
            cory = 18
        else:
            corx = 13
            cory = 15

    elif last == 'k':
        if second_last == 'w':
            corx = 12
            cory = 18
        elif second_last == 'd':
            corx = 14
            cory = 31
        else:
            corx = 13
            cory = 24

    elif last == 'l':
        if second_last == 'p':
            corx = 14
            cory = 1
        elif second_last == 'h':
            corx = 25
            cory = 16
        else:
            corx = 19
            cory = 8

    elif last == 'h':
        if second_last == 'w':
            corx = 14
            cory = 16
        elif second_last == 'l':
            corx = 25
            cory = 16
        elif second_last == 'f':
            corx = 31
            cory = 18
        elif second_last == '1':
            corx = 43
            cory = 14
        elif second_last == '2':
            corx = 45
            cory = 18
        elif second_last == '3':
            corx = 49
            cory = 18
        else:
            corx = 29
            cory = 17

    elif last == 'd':
        if second_last == 'k':
            corx = 14
            cory = 31
        elif second_last == 'f':
            corx = 29
            cory = 31
        else:
            corx = 21
            cory = 31

    elif last == 'f':
        if second_last == 'd':
            corx = 29
            cory = 31
        elif second_last == 'h':
            corx = 31
            cory = 18
        else:
            corx = 30
            cory = 24

    elif last == '1':
        corx = 43
        cory = 14
    elif last == '2':
        corx = 45
        cory = 18
    elif last == '3':
        corx = 49
        cory = 18

    return (corx, cory)


# roomAllowed = []
# roomAllowed.append('h')
# roomAllowed.append('l')
# # roomAllowed.append('+')
# to_door(roomAllowed)
# # savePath = clean_room('l')

# # print(savePath)







