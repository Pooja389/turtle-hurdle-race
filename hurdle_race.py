from turtle import *
import random,time

screen = Screen()
screen.setup(height=400, width=700)
screen.tracer(0)

y_positions = [-180, -140, -100, -60, -20, 0, 20, 60, 100, 140, 180]
colors = ["red", "blue", "green", "yellow", "pink", "black", "orange", "brown"]
all_hurdles = []

player = Turtle()
player.shape("turtle")
player.color("cyan")
player.shapesize(1.5)
player.penup()
player.goto(-200, -180)
player.setheading(90)

def move_up():
    player.forward(10)

screen.listen()
screen.onkey(move_up,"Up")

def create_hurdle():
    hurdle = Turtle()
    hurdle.shape("square")
    hurdle.color(random.choice(colors))
    hurdle.shapesize(0.8,2,2)
    hurdle.penup()
    hurdle.goto(-360,random.choice(y_positions))
    all_hurdles.append(hurdle)

def move_hurdle():
    for hurdle in all_hurdles:
        hurdle.forward(5)
        if hurdle.distance(player) < 28 or player.ycor() > 190:
                return False
    return True
game_on = True   


while game_on:
    screen.update()
    x = random.randint(6,10)
    if x == 8:
        create_hurdle()
    game_on = move_hurdle()    
    if game_on == False:
        if player.xcor() > 190:
            screen.textinput(title= f"game finished",prompt = f"You won, type and press 'ok'")
        else:
            screen.textinput(title= f"game over",prompt = f"You lose, type and press 'ok'")
            screen.bye()



    time.sleep(0.05)  

