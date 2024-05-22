# Written by Yee Shen Teoh

from math import pi, cos
from time import sleep
from amino import SceneWin, QuatTrans, SceneGraph, Geom, GeomOpt, Vec3, YAngle, XAngle
from robot_map import *

def HouseScene(sg, parent):
    height = .5
    wallThick = .1
    color = (1,1,1)
    wall1Dim = [3.0*2+.1, wallThick, height]
    sg.add_frame_fixed(
        parent,
        "wall1",
        tf=QuatTrans((1, (0, 1.7, height/2))),
        geom=Geom.box({
            "color": color
        }, wall1Dim)
    )
    wall2Dim = [wallThick, 1.7*2 +.1, height]
    sg.add_frame_fixed(
        parent,
        "wall2",
        tf=QuatTrans((1, (-3.0, 0, height/2))),
        geom=Geom.box({
            "color": color
        }, wall2Dim))
    wall3Dim = [wallThick, 1.7*2 +.1, height]
    sg.add_frame_fixed(
        parent,
        "wall3",
        tf=QuatTrans((1, (3.0, 0, height/2))),
        geom=Geom.box({
            "color": color
        }, wall3Dim))
    wall4Dim = [3.0*2 +.1, wallThick, height]
    sg.add_frame_fixed(
        parent,
        "wall4",
        tf=QuatTrans((1, (0, -1.7, height/2))),
        geom=Geom.box({
            "color": color
        }, wall4Dim))

    wall5Dim = [wallThick, 0.55*2+.1, height]
    sg.add_frame_fixed(
        parent,
        "wall5",
        tf=QuatTrans((1, (1.5, -0.75, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall5Dim))
    wall6Dim = [.5*2+.1, wallThick, height]
    sg.add_frame_fixed(
        parent,
        "wall6",
        tf=QuatTrans((1, (2.4, -0.7, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall6Dim))
    
    wall7Dim = [.5*2+.1, wallThick, height]
    sg.add_frame_fixed(
        parent,
        "wall7",
        tf=QuatTrans((1, (2.4, .2, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall7Dim))

    wall8Dim = [wallThick, 0.55*2+.1, height]
    sg.add_frame_fixed(
        parent,
        "wall8",
        tf=QuatTrans((1, (1.5, 0.75, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall8Dim))

    wall9Dim = [wallThick, 0.55*2+.1, height]
    sg.add_frame_fixed(
        parent,
        "wall9",
        tf=QuatTrans((1, (0, 0.75, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall9Dim))
    
    wall10Dim = [wallThick, 0.7*2+.1, height]
    sg.add_frame_fixed(
        parent,
        "wall10",
        tf=QuatTrans((1, (-0.6, 0.9, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall10Dim))
    
    wall11Dim = [wallThick, 0.7*2+.1, height]
    sg.add_frame_fixed(
        parent,
        "wall11",
        tf=QuatTrans((1, (-1.8, 0.9, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall11Dim))
    
    wall12Dim = [0.65*2+.1, wallThick, height]
    sg.add_frame_fixed(
        parent,
        "wall12",
        tf=QuatTrans((1, (0.75, 0.2, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall12Dim))
    
    wall13Dim = [0.5*2+.1, wallThick, height]
    sg.add_frame_fixed(
        parent,
        "wall13",
        tf=QuatTrans((1, (-0.9, 0.2, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall13Dim))
    
    wall14Dim = [0.35*2+.1, wallThick, height]
    sg.add_frame_fixed(
        parent,
        "wall14",
        tf=QuatTrans((1, (-2.55, 0.2, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall14Dim))
    
    wall15Dim = [wallThick, 0.85*2+.1, height]
    sg.add_frame_fixed(
        parent,
        "wall15",
        tf=QuatTrans((1, (-2.4, -0.75, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall15Dim))
    
    wall16Dim = [0.35*2+.1, wallThick, height]
    sg.add_frame_fixed(
        parent,
        "wall16",
        tf=QuatTrans((1, (-1.95, -0.2, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall16Dim))

    wall17Dim = [0.2*2+.1, wallThick, height]
    sg.add_frame_fixed(
        parent,
        "wall17",
        tf=QuatTrans((1, (-0.9, -0.2, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall17Dim))
    
    wall18Dim = [wallThick, 0.7*2+.1, height]
    sg.add_frame_fixed(
        parent,
        "wall18",
        tf=QuatTrans((1, (-1.2, -0.9, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall18Dim))
    
    wall19Dim = [wallThick, 0.7*2+.1, height]
    sg.add_frame_fixed(
        parent,
        "wall19",
        tf=QuatTrans((1, (-0.6, -0.9, height/2))),
        geom=Geom.box({
            "color": (1,0,0)
        }, wall19Dim))