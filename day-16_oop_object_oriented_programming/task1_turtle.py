from turtle import Turtle, Screen

timmy = Turtle()
ice = Turtle()
print(timmy, ice)
timmy.shape("turtle")
timmy.color("chartreuse")

timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()