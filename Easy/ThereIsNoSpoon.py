import sys
import math

def check_node(to_the_right, y, x, width, height):
    axe = x if to_the_right else y
    length = width if to_the_right else height

    i = 1

    while (axe + i < length):
        node = list_line[y][x+i] if to_the_right else list_line[y+i][x]
        if node == "0" and to_the_right:
            return str(x+i)+" "+str(y)+" "
        elif node == "0" and not to_the_right:
            return str(x)+" "+str(y+i)+" "
        i = i + 1
    return str(-1)+" "+str(-1)+" "

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
list_line = list()
for i in range(height):
    line = input()  # width characters, each either 0 or .
    list_line.append(line)

for y in range(height):
    for x in range(width):
        node_information = ""
        if list_line[y][x] == "0":
            node_information += str(x)+" "+str(y)+" "
            node_information += check_node(True, y, x, width, height)
            node_information += check_node(False, y, x, width, height)

            print(node_information)
