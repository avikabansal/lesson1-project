import turtle 
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(500,500)
polygon=turtle.Turtle()
num_sides=3
side_len=70
angle=360.0/num_sides
for i in range(num_sides):
    polygon.forward(side_len)
    polygon.right(angle)
turtle.done()