from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.level = 1

    def update(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def endgame(self):

        self.goto(0, -50)
        self.write("You lost :(", align="center",font=("Courier", 48, "bold"))
