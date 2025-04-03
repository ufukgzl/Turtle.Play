import turtle
import random

screen = turtle.Screen()
turtle.bgcolor("light green")
FONT = ("Arial", 24, "normal")
score = 0
game_over = False
scor_turtle = None

countdown_turtle = turtle.Turtle()
countdown_turtle.color("red")

turtle_turtle = turtle.Turtle()



def score_turtle():
    top_height = screen.window_height() / 2
    y = top_height * 0.85

    global scor_turtle
    scor_turtle = turtle.Turtle()
    scor_turtle.color("dark orange")
    scor_turtle.hideturtle()
    scor_turtle.penup()
    scor_turtle.goto(0, y)
    scor_turtle.write("Score: 0", align="center", font=FONT)


def turtle_maker():
    global turtle_turtle

    def hand_click(x, y):
        #print (x,y)
        global score
        score += 1
        scor_turtle.clear()
        scor_turtle.write("Score: {}".format(score), align="center", font=FONT)

    turtle_turtle.onclick(hand_click)
    turtle_turtle.color("dark green")
    turtle_turtle.shape("turtle")
    turtle_turtle.turtlesize(2)
    turtle_turtle.penup()

    def turtle_move():
        if not game_over:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            turtle_turtle.hideturtle()
            turtle_turtle.goto(x, y)
            turtle_turtle.showturtle()
            turtle.ontimer(turtle_move, 800)

    turtle_move()



def countdown(time):
    global turtle_turtle
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.goto(0,220)
    countdown_turtle.clear()


    if time > 0 :
        countdown_turtle.clear()
        countdown_turtle.write("Time:  {}".format(time), align="center", font=FONT)
        screen.ontimer(lambda: countdown(time-1), 1000)


    else :
        game_over = True
        countdown_turtle.clear()
        turtle_turtle.hideturtle()
        countdown_turtle.write("Game Over !", align = "center", font = FONT )

turtle.tracer(0)

score_turtle()
countdown(10)
turtle_maker()

turtle.tracer(1)

turtle.mainloop()