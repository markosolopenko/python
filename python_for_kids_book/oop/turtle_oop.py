import time
import turtle

t1 = turtle.Pen()
t2 = turtle.Pen()
t3 = turtle.Pen()
t4 = turtle.Pen()
time.sleep(1)

t1.forward(100)
t2.forward(100)
t1.left(90)
t2.right(90)
t1.forward(40)
t2.forward(40)
t1.right(90)
t2.left(90)
t1.forward(25)
t2.forward(25)

time.sleep(1)


t3.forward(80)
t4.forward(80)
t3.left(90)
t4.right(90)
t3.forward(70)
t4.forward(70)
t3.right(90)
t4.left(90)
t3.forward(60)
t4.forward(60)

time.sleep(1)

print(dir(turtle))


