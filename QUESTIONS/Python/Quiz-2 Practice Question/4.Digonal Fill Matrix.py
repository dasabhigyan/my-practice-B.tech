# Problem: Diagonal Fill Matrix
# Difficulty: HARD | Max Score: 75
#
# Read two integers R and C. Fill an R x C matrix with the numbers 1, 2, 3, ...,
# R x C along its anti-diagonals. An anti-diagonal is made of the cells with the
# same value of i + j (i is the row number and j is the column number, both
# counting from 0).
# First fill the diagonal i + j = 0, then i + j = 1, then i + j = 2, and so on
# up to the last diagonal. Inside one diagonal, go from the top row to the
# bottom row (the cell with the smaller i comes first). Then print the matrix,
# one row per line, with the numbers of a row separated by single spaces.
#
# For R = 3 and C = 3 the matrix is:
# 1 2 4
# 3 5 7
# 6 8 9
#
# Input Format:
# A single line with two integers R and C.
#
# Output Format:
# Print R lines with C numbers each, separated by single spaces.
#
# Constraints:
# - 1 <= R <= 10
# - 1 <= C <= 10
#
# Example 1:
# Input:
# 3 3
#
# Output:
# 1 2 4
# 3 5 7
# 6 8 9
# Explanation: The diagonals are filled in this order: (0,0) gets 1; (0,1) and
# (1,0) get 2 and 3; (0,2), (1,1) and (2,0) get 4, 5 and 6; (1,2) and (2,1)
# get 7 and 8; (2,2) gets 9.
#
# Example 2:
# Input:
# 2 4
#
# Output:
# 1 2 4 6
# 3 5 7 8
# Explanation: The diagonals of a 2 x 4 matrix are: (0,0) gets 1; (0,1) and
# (1,0) get 2 and 3; (0,2) and (1,1) get 4 and 5; (0,3) and (1,2) get 6 and 7;
# (1,3) gets 8.

# --- Solution using while loops ---

r, c = map(int, input().split())

# Initialize R x C matrix with 0s using a while loop
grid = []
row_idx = 0
while row_idx < r:
  row = []
  col_idx = 0
  while col_idx < c:
    row.append(0)
    col_idx += 1
  grid.append(row)
  row_idx += 1

# Fill anti-diagonals d = i + j from 0 up to (R - 1) + (C - 1)
num = 1
d = 0
max_d = r + c - 2
while d <= max_d:
  # Traverse row i from top (0) to bottom (r - 1)
  i = 0
  while i < r:
    j = d - i
    # Check if column j falls inside valid bounds [0, c - 1]
    if 0 <= j < c:
      grid[i][j] = num
      num += 1
    i += 1
  d += 1

# Print each row of the filled matrix with space-separated values
out_r = 0
while out_r < r:
  out_c = 0
  line_parts = []
  while out_c < c:
    line_parts.append(str(grid[out_r][out_c]))
    out_c += 1
  print(" ".join(line_parts))
  out_r += 1