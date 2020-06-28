import turtle


def squar(length):
    bob = turtle.Turtle()

    for i in range(4):
        bob.fd(len)
        bob.lt(90)

    turtle.mainloop()


def polygon(n, length):
    bob = turtle.Turtle()

    for i in range(n):
        bob.fd(length)
        bob.lt(360 / n)

    turtle.mainloop()


# squr(200)
polygon(360, 2)
#polygon(36,2)
