import turtle
import random

t = turtle.Turtle()

t.color("light green")

turtle.shape("turtle")
turtle.color("red")
turtle.pensize(10)

FONT = ('Arial', 30, 'normal')

def countdown(time):
    screen.onclick(None)  # disable click until countdown completes
    turtle.clear()

    if time > 0:
        t.color("red")
        t.penup()
        t.goto(0, 250)
        t.write(time, align='center', font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)


        def move_random():
            x = random.randint(-300, 300)
            y = random.randint(-300, 300)
            turtle.penup()
            turtle.goto(x, y)

            t.clear()

        for i in range(10):
            move_random()


    else:
        turtle.write("Click Screen", align='center', font=FONT)
        screen.onclick(lambda x, y: countdown(30))

turtle.write("Click Screen", align= "center", font=FONT)

screen = turtle.Screen()
screen.onclick(lambda x, y: countdown(30))
screen.mainloop()