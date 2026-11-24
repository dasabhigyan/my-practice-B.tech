# Problem: Square Envelope With Border and Diagonals
# Difficulty: MEDIUM | Max Score: 50
#
# Read an integer n. Print an n x n grid of characters. A cell is a star '*'
# if at least one of these is true, and a space otherwise:
# 1. it is on the border: it is in the first row, the last row, the first column
#    or the last column
# 2. it is on the main diagonal (row number = column number)
# 3. it is on the other diagonal (row number + column number = n - 1, counting
#    rows and columns from 0)
#
# Input Format:
# A single integer n.
#
# Output Format:
# Print n lines of n characters each (stars and spaces). Every line ends with a
# star, because the last column is always on the border.
#
# Constraints:
# - 1 <= n <= 30
#
# Example 1:
# Input:
# 5
#
# Output:
# *****
# ** **
# * * *
# ** **
# *****
# Explanation: n = 5. The first and last rows are all stars. In row 2 the stars
# are the two border cells and the two diagonal cells next to them, so the
# middle is the only space. In the middle row, the stars are the border cells
# and the centre.
#
# Example 2:
# Input:
# 6
#
# Output:
# ******
# **  **
# * ** *
# * ** *
# **  **
# ******
# Explanation: n = 6. The two diagonals do not touch each other: each inner row
# has two diagonal cells, which are separated from each other and from the
# border cells by spaces.

# --- Solution using while loops ---

n = int(input())

# Outer while loop iterates through row index r from 0 to n - 1
r = 0
while r < n:
  line = ""
  # Inner while loop iterates through column index c from 0 to n - 1
  c = 0
  while c < n:
    on_border = (r == 0) or (r == n - 1) or (c == 0) or (c == n - 1)
    on_main_diag = (r == c)
    on_anti_diag = (r + c == n - 1)

    if on_border or on_main_diag or on_anti_diag:
      line += "*"
    else:
      line += " "
    c += 1

  print(line)
  r += 1