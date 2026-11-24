# Problem: Plus Sign
# Difficulty: EASY | Max Score: 25
#
# Read an odd integer n. Print an n x n grid that shows a plus sign: every cell
# of the middle row and of the middle column is *, and every other cell is .
#
# Input Format:
# A single odd integer n.
#
# Output Format:
# Print n lines of n characters each.
#
# Constraints:
# - 1 <= n <= 49
# - n is odd
#
# Example 1:
# Input:
# 5
#
# Output:
# ..*..
# ..*..
# *****
# ..*..
# ..*..
# Explanation: The middle row and the middle column are number 2 (counting from
# 0). Every cell that is in row 2 or in column 2 is *, the rest are dots.
#
# Example 2:
# Input:
# 3
#
# Output:
# .*.
# ***
# .*.
# Explanation: The middle row and the middle column are number 1: .*. / *** / .*.

# --- Solution using while loops ---

n = int(input())

# Middle index (0-based) for an odd integer n is n // 2
mid = n // 2

# Outer while loop iterates through row index i from 0 to n - 1
i = 0
while i < n:
  row_str = ""
  # Inner while loop iterates through column index j from 0 to n - 1
  j = 0
  while j < n:
    # Any cell on the middle row or middle column is '*', otherwise '.'
    if i == mid or j == mid:
      row_str += "*"
    else:
      row_str += "."
    j += 1

  print(row_str)
  i += 1