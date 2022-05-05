#Turtle functioning program for creating Initials
#Bert Williams
#CTI-110
#April 25, 2022
#
#*******Pseuodo Code**********
# Function (import turtle) to apply turtle program perameters
# Funtion win.= turtle.Screen() creates the window panel for the turtle program
# Function win.bgcolor changes the color of the backdrop
# Dispaly title of operation
# Display of the line can be changed with bo.color("")
# "First Initial"
# Using "Left" "Rignt" to create the degrees of the turn
# Using "Forward" to draw the distance of each line
# On each turn you have to comeplete the connection with "forward"
# Comeplete the code of turtle with win.mainloop()
#*****************************

import turtle
win= turtle.Screen()
win.bgcolor("black")
win.title("Cowabunga!")

bo= turtle.Turtle()
bo.color("purple")
bo.pensize(3)
bo.shape("turtle")

bo.penup()
bo.left(180)
bo.forward(200)
bo.pendown()
#First Initial B
bo.right(90)
bo.forward(200)
bo.right(120)
bo.forward(100)
bo.right(120)
bo.forward(100)
bo.left(120)
bo.forward(100)
bo.right(120)
bo.forward(100)

#Second Initial O
bo.penup()
bo.left(150)
bo.forward(200)
bo.pendown()
bo.left(135)
bo.forward(125)
bo.right(90)
bo.forward(125)
bo.right(90)
bo.forward(125)
bo.right(90)
bo.forward(125)

#Third Initial W
bo.penup()
bo.left(135)
bo.forward(180)
bo.pendown()
bo.left(115)
bo.forward(200)
bo.right(180)
bo.forward(200)
bo.left(135)
bo.forward(100)
bo.right(135)
bo.forward(100)
bo.left(135)
bo.forward(200)

win.mainloop()
