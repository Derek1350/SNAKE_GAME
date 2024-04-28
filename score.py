from turtle import Turtle
score=Turtle()
score.hideturtle()
class Score:
    def update_score(self,i_score):
        self.i_score=i_score
        score.clear()
        score.color("white")
        score.penup()
        score.goto(0,300)
        score.write(f"Score: {i_score}", align="center", font=("Arial", 24, "normal"))
    def high_score():
        pass