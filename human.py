# Written by Yee Shen Teoh

from math import pi, cos
from time import sleep
from amino import SceneWin, QuatTrans, SceneGraph, Geom, GeomOpt, Vec3, YAngle, XAngle
from robot_map import *

def human(sg, parent):
    # add_frame_prismatic
    height = .5
    radius = .1
    sg.add_frame_prismatic(parent, "xDir_h", axis=(1,0,0))
    sg.add_frame_prismatic("xDir_h", "yDir_h", axis=(0,1,0),
                            geom=Geom.cylinder({
                                "color": (1,1,0)
                                }, height, radius)
                           )


def human_mem():
    return start()