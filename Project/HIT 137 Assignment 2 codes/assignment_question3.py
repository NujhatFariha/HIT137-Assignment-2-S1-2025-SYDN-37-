import turtle

def recursive_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
        return

    length = length / 3

    recursive_edge(length, depth - 1)
    turtle.right(60)

    recursive_edge(length, depth - 1)
    turtle.left(120)

    recursive_edge(length, depth - 1)
    turtle.right(60)

    recursive_edge(length, depth - 1)

def draw_polygon(sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        recursive_edge(length, depth)
        turtle.right(angle)

sides = int(input("Enter the number of sides: "))
length = float(input("Enter the side length: "))
depth = int(input("Enter the recursion depth: "))

turtle.speed(0)
turtle.hideturtle()

screen = turtle.Screen()
screen.setup(900, 900)

draw_polygon(sides, length, depth)

turtle.done()