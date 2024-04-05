import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car = Player()
scoreboard = Scoreboard()
car_manager1 = CarManager()
screen.listen()
game_is_on = True
key_states = {"Up": False}


def set_key_state(key, state):
    key_states[key] = state


def handle_key_press():
    if key_states["Up"]:
        car.up()


def handle_key_release():
    if not key_states["Up"]:
        car.stop()


screen.onkeypress(lambda: set_key_state("Up", True), "Up")
screen.onkeyrelease(lambda: set_key_state("Up", False), "Up")
car_manager1.create()

while game_is_on:
    scoreboard.update()
    time.sleep(0.1)
    screen.update()
    handle_key_press()
    handle_key_release()
    if car_manager1.VEHICLES[-1].xcor() <= 260:
        car_manager1.create()
    car_manager1.move()
    for vehicle in car_manager1.VEHICLES:
        if car.distance(vehicle) <= 20:
            game_is_on = False
            scoreboard.endgame()

    if car.ycor() >= 280:
        time.sleep(0.5)
        scoreboard.level += 1
        car.startpos()
        car_manager1.nextlevel()


screen.exitonclick()
