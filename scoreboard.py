from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("snake_game/score.txt") as file:
            self.high_score = int(file.read())
        # self.high_score = 0
        self.color("white")
        self.penup() #hides the line
        self.goto(0,270) #goes to location 
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"score: {self.score} | High Score: {self.high_score}",align="center", font=("Courier", 24,"normal"))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align="center", font=("Courier", 24,"normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snake_game/score.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.update_score()    
        


 
        