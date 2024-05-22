# Written by Yee Shen Teoh

from math import pi, cos
from time import sleep
from amino import SceneWin, QuatTrans, SceneGraph, Geom, GeomOpt, Vec3, YAngle, XAngle
from robot_map import *
from robot import *
from human import *
from A_star import *
from Q_learning import *
from Coverage_path_planning import *
# from room_clean_plan import *
from house import *

# randomly generate probability of where human is
def random_gen(n):
    probability = []

    maxVal = 100

    for i in range(n-1):
        if maxVal == 0:
            ran = 0
        elif maxVal > 0 and i == n-2:
            ran = maxVal
        else:
            ran = random.randint(1,min(maxVal, 70))
        maxVal = maxVal-ran
        probability.append(ran)
    random.shuffle(probability)
    probability.insert(4, 0)
    return probability

# Human randomly choose a room to moved to.
def human_move(probability, number):
    ran_number = random.randint(1,100)
    count = 0
    for i in range(10):
        if probability[number][i] != 0:
            count = count + probability[number][i]
            if count > ran_number:
                return i

    return i


map = robot_mem()
map.printMap()

win = SceneWin(start=False)

sg = SceneGraph()

sg.add_frame_fixed(
    "",
    "grid",
    geom=Geom.grid({
        "color": (0,0,1)
    }, [3.0,1.7], [.1,.1], .005))

HouseScene(sg, "grid")
robot(sg, "grid")
human(sg, "grid")
sg.init()
win.scenegraph = sg
win.start(True)

# Moving one block takes 1 unit time
# 1 unit time is 10 sleepTIme
# 1 unit space is .1
# start pos for robot is x=0, y=0, 
# but for the map it is width=29, height=16 
sleepTime = .01
x_r = 0
y_r = 0

x_h = 1
y_h = 1

probability_h = []
for i in range(10):
    probability_h.append(random_gen(10))


# probability_h = [[0, 0, 100, 0, 0, 0, 0, 0, 0, 0], [0, 0, 100, 0, 0, 0, 0, 0, 0, 0], [0, 0, 100, 0, 0, 0, 0, 0, 0, 0], [0, 0, 100, 0, 0, 0, 0, 0, 0, 0], [0, 0, 100, 0, 0, 0, 0, 0, 0, 0],[0, 0, 100, 0, 0, 0, 0, 0, 0, 0],[54, 10, 0, 0, 0, 0, 8, 28, 0, 0], [70, 15, 6, 0, 0, 0, 3, 1, 0, 5], [12, 18, 14, 20, 0, 14, 16, 2, 1, 3], [58, 12, 7, 1, 0, 2, 4, 2, 4, 10]]

# probability_h = [[100, 50, 50, 10, 0, 0, 50, 50, 50, 50], [0, 0, 0, 100, 0, 0, 0, 0, 0, 0], [0, 0, 0, 100, 0, 0, 0, 0, 0, 0], [0, 0, 100, 0, 0, 0, 0, 0, 0, 0], [0, 0, 100, 0, 0, 0, 0, 0, 0, 0],[0, 0, 100, 0, 0, 0, 0, 0, 0, 0],[54, 10, 0, 0, 0, 0, 8, 28, 0, 0], [70, 15, 6, 0, 0, 0, 3, 1, 0, 5], [12, 18, 14, 20, 0, 14, 16, 2, 1, 3], [58, 12, 7, 1, 0, 2, 4, 2, 4, 10]]

# probability_h = [[100, 0, 150, 0, 120, 50, 50, 50, 50, 50], [5, 5, 0, 5, 0, 100, 1, 5, 5, 5], [0, 0, 0, 100, 0, 0, 0, 0, 0, 0], [0, 0, 100, 0, 0, 0, 0, 0, 0, 0], [0, 0, 100, 0, 0, 0, 0, 0, 0, 0],[0, 0, 100, 0, 0, 0, 0, 0, 0, 0],[54, 10, 0, 0, 0, 0, 8, 28, 0, 0], [70, 15, 6, 0, 0, 0, 3, 1, 0, 5], [12, 18, 14, 20, 0, 14, 16, 2, 1, 3], [58, 12, 7, 1, 0, 2, 4, 2, 4, 10]]

room_ind = human_move(probability_h, 0)


startRoom_r = 'h'

room = ['p','w','k','l','h','d','f','1','2','3']
availableRoom = ['p','w','k','l','h','d','f','1','2','3']

roomAllowedHuman = ['p','w','k','l','h','d','f','1','2','3','+']
startRoom_h = roomAllowedHuman[room_ind]
endRoom_h = roomAllowedHuman[room_ind]

steps_r = []
steps_h = []

human_wait = 250
human_count = human_wait
human_prob = -1

start_cleaning = False
clean_r = []
pre_pos = (29, 16)

human_current = startRoom_h
move_to_end = True
human_cur_walking = True

clean_interupted = False

force_wait = False

drove_pass_human = False
waiting = False

passage_block = False

sleep(20)

while win.is_runnining():
    
    if len(steps_h) > 0:
        human_cur_walking = True
        curAct = steps_h.pop(0)
        x_h_next, y_h_next = converMemToSim(curAct)
        inr_x_h = (x_h_next-x_h)/10
        inr_y_h = (y_h_next-y_h)/10

        if human_current != MemToRoom(curAct) and MemToRoom(curAct) != '+':
            human_current = MemToRoom(curAct)
            # print("humean walking in " + human_walking)

        if len(steps_h) == 0:
            human_cur_walking = False
        
    elif human_count == human_wait and human_prob < 9:
        human_prob = human_prob+1
        # print(human_prob)
        room_ind = human_move(probability_h, human_prob)
        endRoom_h = roomAllowedHuman[room_ind]

        human_count = 0
        startpos_h = roomToMem(startRoom_h)
        goal_h = roomToMem(endRoom_h)

        startRoom_h = endRoom_h
        steps_h = AStar(startpos_h, goal_h, map, roomAllowedHuman)
        x_h, y_h = converMemToSim(startpos_h)

        inr_x_h = 0
        inr_y_h = 0
        
    
        # human_current = startRoom_h
        # print("human is in " + human_current)

    else:
        
        inr_x_h = 0
        inr_y_h = 0

    if len(steps_r) > 0 and len(clean_r) == 0:

        curAct = steps_r[0]
        if len(steps_r) > 1:
            if MemToRoom(curAct) == '+' and MemToRoom(steps_r[1]) == human_current and not human_cur_walking:
                print("passage block, reroute")
                passage_block = True
            elif MemToRoom(curAct) != '+' and MemToRoom(steps_r[1]) == '+':
                passage_block = False
                # print("passage unblocked")
        
        if not passage_block:
            if MemToRoom(curAct) != '+' and MemToRoom(curAct) == human_current and human_cur_walking:
                if drove_pass_human == False:
                    print("drove pass human in room " + human_current +", wait...")
                    inr_x_r = 0
                    inr_y_r = 0
                    drove_pass_human = True

            else:
                drove_pass_human = False
                curAct = steps_r.pop(0)
                x_r_next, y_r_next = converMemToSim(curAct)
                inr_x_r = (x_r_next-x_r)/10
                inr_y_r = (y_r_next-y_r)/10
                pre_pos = curAct
            
            if len(steps_r) == 0 and move_to_end:
                start_cleaning = True

            pre_room = MemToRoom(curAct)

        else:
            steps_r = []

            startpos_r = pre_pos
            roomAllowed = ['p','w','k','l','h','d','f','1','2','3','+']
            roomAllowed.remove(human_current)
            goal_r = roomToMem(endRoom_r)
            steps_r = AStar(startpos_r, goal_r, map, roomAllowed)
            x_r, y_r = converMemToSim(startpos_r)
            inr_x_r=0
            inr_y_r=0
            passage_block = False



    elif start_cleaning:
        cleaning_room = endRoom_r
            
        clean_steps = clean_room(cleaning_room)

        move_temp = AStar(pre_pos, clean_steps[0], map, roomAllowedHuman)

        clean_r = move_temp + clean_steps

        while pre_pos == clean_r[0]:
            clean_r.pop(0)
        start_cleaning = False

    elif not start_cleaning and len(clean_r) > 0:
        if (cleaning_room == human_current and not human_cur_walking) and not force_wait:
            waiting = False
            print("human found in  room "+ cleaning_room)
            
            clean_interupted = True
            if len(availableRoom) == 0:
                # wait on spot until human gone 
                print("Last room to clean")
                force_wait = True
                clean_interupted = False
            else:
                clean_r = []
        elif (cleaning_room == human_current and human_cur_walking) or (force_wait and cleaning_room == human_current): # wait for human to finish walking
            if waiting == False:
                inr_x_r = 0
                inr_y_r = 0
                print("wait...")
                waiting = True
            pass
        else:
            waiting = False
            curAct = clean_r.pop(0)
            x_r_next, y_r_next = converMemToSim(curAct)
            inr_x_r = (x_r_next-x_r)/10
            inr_y_r = (y_r_next-y_r)/10
            pre_pos = curAct

        if len(clean_r) == 0 and not clean_interupted:
            print('cleaning finish for room ' + cleaning_room)
            # availableRoom.remove(endRoom_r)
            # print(availableRoom)

        
    elif (len(availableRoom) > 0 and len(steps_r) == 0) or clean_interupted:
        if human_prob >= 10:
            prob_temp = 9
        else:
            prob_temp = human_prob

        # print(probability_h[prob_temp])



        roomAllowed = best_room(room, startRoom_r, len(room), probability_h[prob_temp].copy(), availableRoom)
        
        if clean_interupted:
            availableRoom.append(endRoom_r)
            clean_interupted = False
            # if len(roomAllowed) == 0:
            #     roomAllowed = best_room(room, startRoom_r, len(room), probability_h[prob_temp].copy(), availableRoom)
            #     print("no room")

        endRoom_r = roomAllowed[len(roomAllowed)-1]

        startpos_r = pre_pos
        if len(roomAllowed) > 1:
            goal_r = to_door(roomAllowed)
        else:
            goal_r = (29, 16)

        roomAllowed.append('+') 
        availableRoom.remove(endRoom_r)
        startRoom_r = endRoom_r
        steps_r = AStar(startpos_r, goal_r, map, roomAllowed)
        x_r, y_r = converMemToSim(startpos_r)
        inr_x_r=0
        inr_y_r=0

        print("moving to room "+ endRoom_r)
        print(availableRoom)
        print(roomAllowed)
        print(probability_h[prob_temp])

    elif move_to_end:
        # print("here")
        if human_prob >= 6:
            prob_temp = 5
        else:
            prob_temp = human_prob

        # print(probability_h[prob_temp])
        availableRoom.append('h')
        roomAllowed = best_room(room, startRoom_r, len(room), probability_h[prob_temp].copy(), availableRoom)
        endRoom_r = roomAllowed[len(roomAllowed)-1]
        

        startpos_r = pre_pos
        goal_r = (29, 16)

        roomAllowed.append('+') 
        availableRoom.remove(endRoom_r)
        startRoom_r = endRoom_r
        steps_r = AStar(startpos_r, goal_r, map, roomAllowed)
        x_r, y_r = converMemToSim(startpos_r)
        inr_x_r=0
        inr_y_r=0
        # print(steps_r)
        move_to_end = False
        print("FInish cleaning")

    else:
        inr_x_r = 0
        inr_y_r = 0        


    for i in range(10):
        x_r = x_r + inr_x_r
        y_r = y_r + inr_y_r

        x_h = x_h + inr_x_h
        y_h = y_h + inr_y_h

        win.config = {"xDir_r": x_r, "yDir_r": y_r, "xDir_h": x_h, "yDir_h": y_h}
        sleep(sleepTime)

    human_count = human_count + 1


