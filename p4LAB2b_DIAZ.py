import turtle             # Allows us to use turtles
win = turtle.Screen()      # Creates a playground for turtles
t = turtle.Turtle()
t.color("blue")            # Tell tess to change her color
t.pensize(3) 



t.left(90)
t.forward(100)
t.left(180)
t.forward(200)
t.left(180)
t.forward(100)
t.right(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(180)
t.forward(200)
t.penup()
t.left(90)
t.forward(50)
t.pendown()
t.left(90)
t.forward(200)
t.right(90)

for i in range(8):
    t.forward(45)
    t.right(25)

