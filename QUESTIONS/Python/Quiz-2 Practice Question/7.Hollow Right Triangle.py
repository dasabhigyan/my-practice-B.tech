# Problem: Hollow Right Triangle
# Difficulty: EASY | Max Score: 25
#
# Read an integer n. Print a hollow right-angled triangle of * with n rows,
# aligned to the left. Only the border of the triangle is drawn: the first star
# of every row, the last star of every row, and the whole last row. The inside
# of the triangle is empty (spaces).
#
# Input Format:
# A single integer n.
#
# Output Format:
# Print n lines. Row 1 is a single *. The last row has n stars. Every other row
# has a *, then spaces, then a *. There is no space at the end of any line.
#
# Constraints:
# - 1 <= n <= 20
#
# Example 1:
# Input:
# 5
#
# Output:
# *
# **
# * *
# *  *
# *****
# Explanation: Row 1 is *. Row 2 is **. Rows 3 and 4 have a star at each end
# and 1 and 2 spaces between them. The last row is 5 stars.
#
# Example 2:
# Input:
# 3
#
# Output:
# *
# **
# ***
# Explanation: Row 1 is *. Row 2 is **. The last row (row 3) is 3 stars.

# --- Solution using while loops ---

n = int(input())

# Outer while loop iterates through row i from 1 to n
i = 1
while i <= n:
  line = ""

  if i == 1:
    # Row 1 is a single *
    line = "*"
  elif i == n:
    # Last row has n stars
    cnt = 0
    while cnt < n:
      line += "*"
      cnt += 1
  else:
    # Middle rows (1 < i < n): '*' followed by (i - 2) spaces and '*'
    # For i = 2, i - 2 = 0 spaces -> "**"
    # For i = 3, i - 2 = 1 space  -> "* *"
    # For i = 4, i - 2 = 2 spaces -> "*  *"
    line += "*"
    sp = 0
    while sp < i - 2:
      line += " "
      sp += 1
    line += "*"

  print(line)
  i += 1