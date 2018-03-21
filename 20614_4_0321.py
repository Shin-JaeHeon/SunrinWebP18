import turtle

t = turtle.Pen()

while True:
    i = input("왼쪽 = left, 오른쪽 = right:")
    if i == "left":
        t.left(60)
        t.fd(50)
    elif i == "right":
        t.left(60)
        t.fd(50)


# def right():
#     t.right(45)
#     t.fd(50)
#
#
# def left():
#     t.right(45)
#     t.fd(50)
#
#
# def up():
#     t.right(45)
#     t.fd(50)
#
#
# def down():
#     t.right(45)
#     t.fd(50)
#
#
# turtle.title("")
# turtle.onkey(right, "Right")
# turtle.onkey(up, "Up")
# turtle.onkey(left, "Left")
# turtle.onkey(down, "Down")
# turtle.listen()
# turtle.mainloop()
