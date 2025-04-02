import random
import turtle


screen = turtle.Turtle()
screen.color("light blue")
FONT = ('Arial', 30, "normal")



def countdown(time):
    turtle_time = turtle.Turtle()
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





def turtle_positions():
    my_turtel = turtle.Turtle()
    my_turtel.shape("turtle")
    my_turtel.showturtle()
    my_turtel.color("red")
    my_turtel.pensize(5)

    coordinates_list = []
    screen.onclick(None)
    turtle.clear()
    for i in range(3):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        coordinates_list.append((x, y))

    for (a,b) in coordinates_list:
        #turtle.penup()
        turtle.goto(a,b)





turtle.write("Click Screen", align='center', font=FONT)
screen.onclick(turtle_positions())
screen.onclick(lambda x, y: countdown(30))
screen.mainloop()