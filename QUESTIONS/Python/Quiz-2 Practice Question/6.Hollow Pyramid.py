# Problem: Hollow Pyramid
# Difficulty: MEDIUM | Max Score: 50
#
# Read an integer n. Print a hollow pyramid of * with n rows, centred. Only
# the border of the pyramid is drawn: the two sides and the whole last row. The
# inside is empty (spaces).
#
# Input Format:
# A single integer n.
#
# Output Format:
# Print n lines. Row i starts with n - i spaces. Row 1 is a single *. The last
# row has 2n - 1 stars. Every other row has a *, then spaces, then a *. There
# is no space at the end of any line.
#
# Constraints:
# - 1 <= n <= 20
#
# Example 1:
# Input:
# 5
#
# Output:
#     *
#    * *
#   *   *
#  *     *
# *********
# Explanation: Row 1 has 4 leading spaces and one star. Rows 2, 3 and 4 have
# two stars with 1, 3 and 5 spaces between them. The last row is 2 * 5 - 1 = 9
# stars with no leading space.
#
# Example 2:
# Input:
# 3
#
# Output:
#   *
#  * *
# *****
# Explanation: Row 1 is two spaces and a star. Row 2 is one space, a star, one
# space, a star. The last row is 5 stars.

# --- Solution using while loops ---

n = int(input())

# Outer while loop iterates through row i from 1 to n
i = 1
while i <= n:
  # 1. Leading spaces: n - i spaces
  spaces = ""
  s = 0
  while s < n - i:
    spaces += " "
    s += 1

  # 2. Build row body based on whether it's the top row, last row, or middle row
  body = ""
  if i == 1:
    # Row 1 is a single *
    body = "*"
  elif i == n:
    # Last row has 2n - 1 stars
    cnt = 0
    while cnt < 2 * n - 1:
      body += "*"
      cnt += 1
  else:
    # Middle rows (1 < i < n): '*' followed by 2*i - 3 spaces and '*'
    body += "*"
    inner_sp = 0
    while inner_sp < 2 * i - 3:
      body += " "
      inner_sp += 1
    body += "*"

  print(spaces + body)
  i += 1