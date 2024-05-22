# Written by Yee Shen Teoh

from math import pi, cos
from time import sleep
from amino import SceneWin, QuatTrans, SceneGraph, Geom, GeomOpt, Vec3, YAngle, XAngle
from robot_map import *

#available room:
    # proch
    # laundry
    # kitchen
    # living room
    # Dining 
    # foyer
    # walk way
    # bedroom 1
    # bedroom 2
    # bedroom 3

#start position is x=0, y=0, width is 

def robot_mem():
    return start()
    
def robot(sg, parent):
    # add_frame_prismatic
    height = .05
    radius = .1
    sg.add_frame_prismatic(parent, "xDir_r", axis=(1,0,0))
    sg.add_frame_prismatic("xDir_r", "yDir_r", axis=(0,1,0),
                            geom=Geom.cylinder({
                                "color": (0,1,0)
                                }, height, radius)
                           )
    # sg.add_frame_fixed(
    #     parent,
    #     "robot_cleaner",
    #     tf=QuatTrans((1, (x/10,y/10,height/2))),
    #     geom=Geom.cylinder({
    #         "color": (0,1,0)
    #     }, height, radius)
    # )


    

