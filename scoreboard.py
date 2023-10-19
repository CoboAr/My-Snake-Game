from turtle import Turtle
ALIGNMENT = "center"
FONT = "Arial", 24, "normal"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # Read highest score value from file
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())

        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(x=0,y=250)
        self.self_updatescore()

    def self_updatescore(self):
        self.clear()
        self.write (arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.self_updatescore()

    def increase_score(self):
        self.score+=1
        self.self_updatescore()

    def game_over(self):
        self.goto (0, 0)
        self.write ("GAME OVER", align=ALIGNMENT, font=FONT)

