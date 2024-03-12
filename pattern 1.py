#pyramid
def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2*i - 1))
print_pyramid(10)

#diamond
def print_diamond(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2*i - 1))
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2*i - 1))
print_diamond(10)

#rhombus
def print_rhombus(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "* " * (i + 1))
    for i in range(rows - 2, -1, -1):
        print(" " * (rows - i - 1) + "* " * (i + 1))
print_rhombus(10)

#circle
import math

def print_circle(radius):
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            if math.sqrt(x**2 + y**2) <= radius:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_circle(10)
