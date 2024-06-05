from numpy import size
from Parameter import *
import pygame,random
#class Map():
 
class Directions():
    movemethod=4
    movevector=[[1,0],[0,1],[-1,0],[0,-1],[0,0]]
    # __movevector.append([1,0]) #South
    # __movevector.append([0,1]) #East
    # __movevector.append([-1,0]) #North
    # __movevector.append([0,-1]) #West
    def __init__(self) -> None:
        pass
    
    @classmethod
    def getmove(cls,x):
        return Directions.movevector[x]
    
