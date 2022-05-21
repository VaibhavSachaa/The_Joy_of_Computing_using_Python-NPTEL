# There is a robot which wants to go the charging point to charge itself. The robot moves in a 2-D plane from the
# original point (0,0).  The robot can move toward UP, DOWN, LEFT and RIGHT with given steps. The trace of robot
# movement is shown as the following:

# The trace of robot movement is shown as the following:
#
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
#
# Then, the output of the program should be: 2

# The numbers after the direction are steps. Write a program to compute the distance between the current position
# after a sequence of movement and original point. If the distance is a float, then just print the nearest integer (
# use round() function for that and then convert it into an integer).

# Input Format:
# The first line of the input contains a number n which implies the number of directions to be given.
# The next n lines contain the direction and the step separated by a space.
#
# Output Format:
# Print the distance from the original position to the current position.

import math

pos = [0, 0]
n = int(input())
for i in range(n):
    s = input()
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        pass

print(int(round(math.sqrt(pos[1] ** 2 + pos[0] ** 2))))
