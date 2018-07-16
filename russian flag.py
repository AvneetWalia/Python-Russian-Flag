import turtle

x=turtle.Screen()
x.bgcolor("light green")
x.title("Russian Flag")

ob=turtle.Turtle();

ob.shape("turtle")

ob.up()
ob.goto(-350,300)
ob.down()

for i in range(2):
    ob.fd(150)
    ob.rt(90)
    ob.fd(90)
    ob.rt(90)

ob.color("white")
ob.speed(20)

for i in range(15):
    ob.fd(150)
    ob.rt(90)
    ob.fd(1)
    ob.rt(90)
    ob.fd(150)
    ob.lt(90)
    ob.fd(1)
    ob.lt(90)

ob.color("blue")
for i in range(15):
    ob.fd(150)
    ob.rt(90)
    ob.fd(1)
    ob.rt(90)
    ob.fd(150)
    ob.lt(90)
    ob.fd(1)
    ob.lt(90)

ob.color("red")
for i in range(15):
    ob.fd(150)
    ob.rt(90)
    ob.fd(1)
    ob.rt(90)
    ob.fd(150)
    ob.lt(90)
    ob.fd(1)
    ob.lt(90)

ob.fd(150)
