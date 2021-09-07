from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=235)
        self.update_score()

    def level_up(self):
        self.level += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level} \nHigh Score: {self.high_score}", align="left", font=FONT)

    def reset(self):
        if self.level > self.high_score:
            self.high_score = self.level
            with open("high_score.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.level = 1
        self.update_score()

