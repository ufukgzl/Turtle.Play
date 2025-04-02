import turtle
from turtle import Screen, Turtle


screen = Screen()
screen.bgcolor("light blue")
FONT = ('Arial', 30)


turtle_time = Turtle()
    screen.onclick(None)  # disable click until countdown completes
    turtle_time.clear()
    turtle_time.hideturtle()
    turtle_time.penup()
    turtle_time.goto(0, 250)
    if time > 0:
        turtle_time.write(time,align="center" , font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        turtle_time.write("Click Screen",align="center", font=FONT)
        screen.onclick(lambda x, y: countdown(30))



turtle.write("Click Screen", align='center', font=FONT)
screen = Screen()


screen.onclick(lambda x, y: countdown(30))
screen.mainloop()
