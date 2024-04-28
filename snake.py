import turtle 
import time
import random
from turtle import Turtle,Screen
from snake_move import move
from score import Score
import score as scr 
import snake_move as sm
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
s_score=Score()
sc=Screen()
sc.title("Snake Game")
sc.listen()
sc.bgcolor("black")
sc.tracer(0)
i_score=0
with open("High_score.txt",mode="r") as file:
     line=file.readline()
     var_name,var_value = line.split("=")
     int(var_value)
next=3
m=move()
head=m.turtle_lst[0]
is_game=True
def up():
        if head.heading() != DOWN:
            head.setheading(UP)

def down():
        if head.heading() != UP:
            head.setheading(DOWN)

def left():
        if head.heading() != RIGHT:
            head.setheading(LEFT)

def right():
        if head.heading() != LEFT:
            head.setheading(RIGHT)

sc.onkey(up, "Up")
sc.onkey(down, "Down")
sc.onkey(left, "Left")
sc.onkey(right, "Right")
m.food()
s_score.update_score(i_score)

while is_game:
    sc.update()
    time.sleep(0.1)
    m.movement()
    if(m.turtle_lst[0].distance(sm.khana.xcor(),sm.khana.ycor())<15):
        m.food()
        i_score +=1
        s_score.update_score(i_score)
        next +=1
        m.new_body()
    for i in m.turtle_lst:
        if head==i:
            pass
        elif head.distance(i)<10:
            is_game=False
            if i_score>int(var_value):
                var_value=i_score
            scr.score.goto(0,0)
            scr.score.write(f"GAME OVER High Score:{var_value}", align="center", font=("Arial", 24, "normal"))
            with open("High_score.txt",mode="w") as file:
                file.write(f"High Score = {var_value}")     
            
            break
    m.respawn()  
    

    

        
        

    

        
        
        
        
        











sc.exitonclick()