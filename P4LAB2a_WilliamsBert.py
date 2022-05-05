#Turtle functioning program to create a rectangle and triangle
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
# "Square", "Triangle"
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
bo.color("red")

#Square
bo.left(90)
bo.forward(100)
bo.right(90)
bo.forward(100)
bo.right(90)
bo.forward(100)
bo.right(90)
bo.forward(100)
bo.right(180)
bo.forward(200)

#Triangle
bo.left(60)
bo.forward(100)
bo.right(120)
bo.forward(100)
bo.right(120)
bo.forward(100)


win.mainloop()
