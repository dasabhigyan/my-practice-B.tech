# Problem: Checkerboard Pattern With Condition
# Difficulty: EASY | Max Score: 25
#
# Read two integers R and C. Print a checkerboard grid with R rows and C
# columns. The cell in row i and column j (both counted from 0) is '#' if
# i + j is even, and '.' if i + j is odd. So the top-left cell is always '#'.
#
# Input Format:
# A single line with two integers R and C.
#
# Output Format:
# Print R lines of C characters each.
#
# Constraints:
# 1 <= R <= 20
# 1 <= C <= 20
#
# Example 1:
# Input:
# 3 4
#
# Output:
# #.#.
# .#.#
# #.#.
# Explanation: Row 0 starts with # and alternates: #.#. . Row 1 starts with . :
# .#.#. Row 2 is the same as row 0.
#
# Example 2:
# Input:
# 2 2
#
# Output:
# #.
# .#
# Explanation: Row 0 is #. and row 1 is .#.

# --- Solution using while loops ---

r, c = map(int, input().split())

# Outer while loop iterates through row index i from 0 to R - 1
i = 0
while i < r:
  row_str = ""
  # Inner while loop iterates through column index j from 0 to C - 1
  j = 0
  while j < c:
    # Even (i + j) gives '#', odd (i + j) gives '.'
    if (i + j) % 2 == 0:
      row_str += "#"
    else:
      row_str += "."
    j += 1

  print(row_str)
  i += 1