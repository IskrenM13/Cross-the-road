from turtle import *
import os
import random
os.chdir("D:\\python\\Cross the road")
screen = Screen()
screen.register_shape('americantruck.gif')
screen.register_shape('bigtruck.gif')
screen.register_shape('minivan.gif')
screen.register_shape('supercar.gif')
screen.register_shape('taxi.gif')
screen.register_shape('van.gif')
COLORS = ["americantruck.gif", "bigtruck.gif", "minivan.gif", "supercar.gif", "taxi.gif", "van.gif"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.VEHICLES = []
        self.move_step = STARTING_MOVE_DISTANCE

    def create(self):
        vehicle = Turtle()
        vehicle.shape(random.choice(COLORS))
        vehicle.shapesize(stretch_wid=1, stretch_len=2)
        vehicle.penup()
        vehicle.goto(x=300, y=random.randint(-260, 260))
        vehicle.setheading(180)
        self.VEHICLES.append(vehicle)

    def move(self):
        for vehicle in self.VEHICLES:
            vehicle.forward(self.move_step)

    def nextlevel(self):
        self.move_step += MOVE_INCREMENT
