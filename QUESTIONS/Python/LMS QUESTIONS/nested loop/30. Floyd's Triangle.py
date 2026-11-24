# 30. Floyd's Triangle
# Read an integer n and print Floyd's triangle with n rows. The triangle is filled
# with the consecutive integers 1, 2, 3, ... in order, and row i (counting from 1)
# contains exactly i numbers.
#
# Input Format:
# A single integer n.
#
# Output Format:
# Print n lines. The numbers of a line are separated by a single space, with no
# space at the end of the line.
#
# Constraints:
# 1 <= n <= 20
# Time limit: 2000 ms · Memory: 256 MB
#
# Example 1:
# Input:
# 4
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
#
# Example 2:
# Input:
# 6
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21


n = int(input())

current_number = 1
row = 1

while row <= n:
  col = 1
  line = ""

  while col <= row:
    if col > 1:
      line = line + " "
    line = line + str(current_number)
    current_number = current_number + 1
    col = col + 1

  print(line)
  row = row + 1