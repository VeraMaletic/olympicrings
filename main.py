import turtle



screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("tan")


t = turtle.Turtle()


#circle
t.penup()
t.goto(-80,15)
t.pendown()
t.pencolor("blue")
t.circle(35)





#circle
t.penup()
t.goto(80,15)
t.pendown()
t.pencolor("red")
t.circle(35)



#circle
t.penup()
t.goto(0,15)
t.pendown()
t.pencolor("black")
t.circle(35)



#circle
t.penup()
t.goto(-40,-15)
t.pendown()
t.pencolor("yellow")
t.circle(35)


#circle
t.penup()
t.goto(40,-15)
t.pendown()
t.pencolor("green")
t.circle(35)



t.penup()
t.goto(0,100)
t.pencolor("purple")
t.pendown()
t.write("Winter Olympics", font=("Arial",30, "bold italic"),align="center")


t.penup()
t.goto(0,-100)
t.pencolor("purple")
t.pendown()
t.write("2026", font=("Arial",30, "bold italic"),align="center")






turtle.done()