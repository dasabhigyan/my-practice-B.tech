# Read three integers, one per line: length, breadth, and height of a box.
# Determine the type of the box based on its dimensions:
# - If all three dimensions are equal, print: Cube
# - If any two dimensions are equal, print: Cuboid (Square Base)
# - If all three dimensions are different, print: Cuboid (General)
#
# Input Format:
# Three integers, one per line:
# 1. length
# 2. breadth
# 3. height
#
# Output Format:
# Exactly one line containing the type of the box.


p1 = input()
p2 = input()

if p1 == p2:
    print("Draw")

elif (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
    print("Player 1 wins")

else:
    print("Player 2 wins")