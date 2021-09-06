from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=250)
        self.update_score()

    def level_up(self):
        self.level += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="center", font=FONT)
