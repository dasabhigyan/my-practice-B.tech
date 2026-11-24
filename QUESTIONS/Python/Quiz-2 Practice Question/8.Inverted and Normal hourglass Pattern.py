# Problem: Inverted and Normal Hourglass Pattern
# Difficulty: MEDIUM | Max Score: 50
#
# Read an integer n. Print an hourglass of stars made of 2n - 1 rows:
# 1. The first row has 2n - 1 stars and no leading space.
# 2. Every next row has 2 stars less and 1 more leading space, until the row n,
#    which has a single star.
# 3. After that, the rows grow back: they are the same as the rows above the
#    middle row, in the opposite order (the middle row is not repeated).
#
# Input Format:
# A single integer n.
#
# Output Format:
# Print the 2n - 1 rows of the hourglass. Rows have no spaces at the end.
#
# Constraints:
# - 1 <= n <= 25
#
# Example 1:
# Input:
# 3
#
# Output:
# *****
#  ***
#   *
#  ***
# *****
# Explanation: n = 3. The rows have 5, 3 and 1 stars (with 0, 1 and 2 leading
# spaces), and then 3 and 5 stars again, which gives 5 rows.
#
# Example 2:
# Input:
# 4
#
# Output:
# *******
#  *****
#   ***
#    *
#   ***
#  *****
# *******
# Explanation: n = 4. The rows have 7, 5, 3 and 1 stars, and then 3, 5 and 7
# stars again, which gives 7 rows.

# --- Solution using while loops ---

n = int(input())

# Build the sequence of row depths d:
# Top half goes 0, 1, ..., n - 1 (leading spaces = d, stars = 2*(n - d) - 1)
# Bottom half goes n - 2, ..., 1, 0 (reversing rows above the middle row)
depths = []
d = 0
while d < n:
  depths.append(d)
  d += 1

d = n - 2
while d >= 0:
  depths.append(d)
  d -= 1

# Print all 2n - 1 rows using a while loop
idx = 0
total_rows = len(depths)
while idx < total_rows:
  depth = depths[idx]

  # 1. Leading spaces: 'depth' spaces (0 on first/last row, n - 1 on middle)
  spaces = ""
  s = 0
  while s < depth:
    spaces += " "
    s += 1

  # 2. Solid stars: 2 * (n - depth) - 1 stars
  star_count = 2 * (n - depth) - 1
  stars = ""
  st = 0
  while st < star_count:
    stars += "*"
    st += 1

  print(spaces + stars)
  idx += 1