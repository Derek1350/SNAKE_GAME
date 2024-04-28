from turtle import Turtle
import random
POSITIONS=[(0,0),(-20,0),(-40,0)]
khana=Turtle()
khana.color("blue")
khana.shape("circle")
khana.shapesize(0.6)
khana.penup()
class move:
    def __init__(self):
        self.turtle_lst=[]
        self.create_body()
        
    def create_body(self):
        for i in POSITIONS:
            self.body(i)
    def body(self,i):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(i)
        self.turtle_lst.append(new_segment)

    def movement(self):
        for snake in range(len(self.turtle_lst)-1,0,-1):
            new_x=self.turtle_lst[snake-1].xcor()
            new_y=self.turtle_lst[snake-1].ycor()
            self.turtle_lst[snake].goto(new_x,new_y)
        self.turtle_lst[0].forward(20)
    def new_body(self):
        self.body(self.turtle_lst[-1].position())

    def food(self):
        food_x=random.randint(-200,200)
        food_y=random.randint(-200,200)
        khana.goto(food_x,food_y)
    def respawn(self):
        if(self.turtle_lst[0].xcor()>350):
            self.turtle_lst[0].goto(-350,self.turtle_lst[1].ycor())
        elif(self.turtle_lst[0].xcor()<-350):
            self.turtle_lst[0].goto(350,self.turtle_lst[1].ycor())
        elif(self.turtle_lst[0].ycor()>350):
            self.turtle_lst[0].goto(self.turtle_lst[1].xcor(),-350)
        elif(self.turtle_lst[0].ycor()<-350):
            self.turtle_lst[0].goto(self.turtle_lst[1].xcor(),350)  