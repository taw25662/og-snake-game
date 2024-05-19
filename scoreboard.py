from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=275)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.high_score = int(open("data.txt").read())
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open('data.txt', mode='w') as file:
                file.write(str(self.score))
        self.high_score = int(open("data.txt").read())
        self.score = 0
        self.update_scoreboard()