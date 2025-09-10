import turtle
turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(500,500)
polygon=turtle.Turtle()
sides=4
len=70
angle=360/sides
for i in range(sides):
    polygon.forward(len)
    polygon.right(angle)
turtle.done()