import turtle as trtl
import random

painter = trtl.Turtle()
#creation of night and grass
painter.speed(0)
painter.goto(-300,0)
painter.pensize(1000)
painter.forward(800)
painter.penup()
painter.goto(-500,-325)
painter.pendown()
painter.pensize(200)
painter.color("green")
painter.forward(1000)
painter.penup()
painter.pensize(1)

# Draw picnic cloth on the grass
painter.goto(-150, -250)
painter.pendown()
painter.color("red")
painter.begin_fill()
# Draw the blanket
for _ in range(2):
    painter.forward(200)
    painter.right(90)
    painter.forward(150)
    painter.right(90)
painter.end_fill()
painter.penup()

# Generate random star positions
star_positions = []
for i in range(50):  # Create 50 random stars
    x = random.randint(-500, 500)  # Random x coordinate
    y = random.randint(10, 450)    # Random y coordinate (lower - can go down to 10)
    star_positions.append((x, y))

# Draw stars at random positions (smaller size)
for pos in star_positions:
    painter.penup()
    painter.goto(pos)
    painter.pendown()
    painter.color("white")
    painter.begin_fill()
    for _ in range(5):
        painter.forward(10)  # Changed from 20 to 10 for smaller stars
        painter.right(144)
    painter.end_fill()
painter.penup() 
# List of firework positions
firework_spots = [(0,0), (200,200), (-200,150), (150,80), (-300,250),
                  (350,150), (-100,300), (50,180), (-350,100), (250,50)]

firework_colors = ["red", "blue", "yellow", "orange", "purple", "cyan", "magenta", "lime", "pink", "white"]
# Draw all fireworks with one loop
for spot in firework_spots:
    painter.color("white")
    painter.shape("circle")
    painter.goto(spot[0], -100)
    painter.speed(1)
    painter.goto(spot[0], spot[1])
    painter.speed(0)
    painter.pendown()
    painter.pensize(1)
    painter.color("white")
    for i in range(12):
        painter.pencolor(firework_colors[i % len(firework_colors)])
        painter.shape("classic")
        painter.speed(0)
        painter.forward(50)
        painter.backward(50)
        painter.left(30)
        painter.forward(50)
        painter.backward(50)
    painter.penup()


# Draw crescent moon at (400, 400)
painter.goto(400, 300)
painter.pendown()
painter.color("yellow")
painter.begin_fill()
painter.circle(50)
painter.end_fill()
# Draw overlapping circle to create crescent
painter.penup()
painter.goto(415, 305)
painter.pendown()
painter.color("black")
painter.begin_fill()
painter.circle(45)
painter.end_fill()
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()