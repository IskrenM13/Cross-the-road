from turtle import *
import os
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
screen = Screen()
os.chdir("D:\\python\\Cross the road")
screen.register_shape('maincar.gif')


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("maincar.gif")
        #self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.movement = MOVE_DISTANCE

    def up(self):
        self.forward(self.movement)

    def stop(self):
        self.setheading(90)

    def startpos(self):
        self.movement += 2
        self.goto(STARTING_POSITION)