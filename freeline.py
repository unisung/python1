import turtle as t
def draw(head, dist):
    t.setheading(head)
    t.forward(dist)

def toleft():
    draw(180, 15)

def toright():
    draw(0, 15)

def toup():
    draw(90, 15)


def todown():
    draw(270, 15)

def move(x, y):
    t.up()
    t.setpos(x, y)
    t.down()


t.shape("turtle")
t.speed(0)
t.onkeypress(toleft, "Left")
t.onkeypress(toright, "Right")
t.onkeypress(toup, "Up")
t.onkeypress(todown, "Down")
t.onscreenclick(move)
t.listen()
t.done()