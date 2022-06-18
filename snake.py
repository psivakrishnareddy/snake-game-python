from re import S
from turtle import Turtle


#CONSTANTS
STARTING_POSITIONS = [(0,0),(-20,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.segments: list[Turtle] #type annotation
        self.head = self.segments[0] #first block is head, ref assigned

    def add_segment(self, position):
        '''adds A block to the snake'''
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        return new_segment

    def extend(self):
        self.segments.append(self.add_segment(self.segments[-1].position()))

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_seg = self.add_segment(position)
            self.segments.append(new_seg)
  

    def move(self):
        # for seg in segments:
        #     seg: Turtle
        #     seg.forward(20)
        for seg_num in range(len(self.segments) - 1 ,0,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE) 
 
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000) # to hide old snake from screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]   

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)            