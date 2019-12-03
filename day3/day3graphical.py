# Just for fun. This isn't to solve it or anything, just visualizes your input.
# NGL Stole the threading technique from stackoverflow
# bc i ain't got time for threading this nonsense
import sys
import queue
import threading
import turtle

ins = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        ins.append(line.split(','))

def wire(t,n):
    for i in ins[n]:
        d = int(i[1:])
        if i[0] == 'R':
            graphics.put((t.setheading, 0))
        elif i[0] == 'L':
            graphics.put((t.setheading, 180))
        elif i[0] == 'U':
            graphics.put((t.setheading, 90))
        elif i[0] == 'D':
            graphics.put((t.setheading, 270))
        graphics.put((t.forward, d // 20))

def process_queue():
    while not graphics.empty():
        x = graphics.get()
        x[0](x[1])

    if threading.active_count() > 1:
        turtle.ontimer(process_queue, 100)

graphics = queue.Queue(1)  # size = number of hardware threads you have - 1

turtle1 = turtle.Turtle('turtle')
turtle1.color(1,0,0)
turtle1.speed('fastest')
turtle1.ht()
thread1 = threading.Thread(target=wire, args=(turtle1,0))
thread1.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
thread1.start()

turtle2 = turtle.Turtle('turtle')
turtle2.color(0,.6,0)
turtle2.speed('fastest')
turtle2.ht()
thread2 = threading.Thread(target=wire, args=(turtle2,1))
thread2.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
thread2.start()

turtle.bgcolor('black')

process_queue()

turtle.exitonclick()