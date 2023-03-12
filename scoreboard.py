from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.ht()
        self.penup()
        self.goto(-280, 260)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", move=False, align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", move=False, align="center", font=FONT)
