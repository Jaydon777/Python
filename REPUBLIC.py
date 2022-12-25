import turtle
tr=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("black")

##GREEN


tr.color("green")
tr.begin_fill()
tr.fillcolor("green")
tr.left(180)
tr.forward(150)
tr.rt(90)
tr.forward(66.6)
tr.rt(90)
tr.forward(300)
tr.rt(90)
tr.forward(66.6)
tr.rt(90)
tr.forward(150)
tr.end_fill()




##white


tr.rt(90)
tr.forward(66.6)
tr.color("white")
tr.left(90)
tr.begin_fill()
tr.fillcolor("white")
tr.forward(150)
tr.rt(90)
tr.forward(66.6)
tr.rt(90)
tr.forward(300)
tr.rt(90)
tr.forward(66.6)
tr.rt(90)
tr.forward(150)
tr.end_fill()




##Blue circle


tr.color("#000080")
tr.begin_fill()
tr.fillcolor("#000080")
tr.circle(-33.3)
tr.end_fill()



##orange


tr.rt(90)
tr.forward(66.6)
tr.color("orange")
tr.left(90)
tr.begin_fill()
tr.fillcolor("orange")
tr.forward(150)
tr.rt(90)
tr.forward(66.6)
tr.rt(90)
tr.forward(300)
tr.rt(90)
tr.forward(66.6)
tr.rt(90)
tr.forward(150)
tr.end_fill()


tr.penup()
tr.left(90)
tr.forward(240)
tr.left(90)

tr.color("#DEB887")
tr.write("HAPPY REPUBLIC DAY !!!",font=("Metropolis",24,"bold"),align="center")
tr.hideturtle()


wn.exitonclick()