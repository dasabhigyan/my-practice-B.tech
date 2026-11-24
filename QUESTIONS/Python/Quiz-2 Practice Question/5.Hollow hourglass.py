# Problem: Hollow Hourglass
# Difficulty: HARD | Max Score: 75
#
# Read an integer n and print a hollow hourglass made of * characters. The
# hourglass has 2n - 1 rows. Number the rows by k: the rows are k = 1, 2, ..., n
# (the top half, going down) and then k = n - 1, ..., 2, 1 (the bottom half).
# So the middle row (k = n) is printed only once.
# Row k starts with k - 1 spaces. After the spaces comes a part of width
# w = 2 * (n - k) + 1:
# 1. if k is 1 or k is n, the part is w stars (a full line)
# 2. otherwise the part is a star, then w - 2 spaces, then a star (only the two
# ends are printed)
#
# Input Format:
# A single integer n.
#
# Output Format:
# Print 2n - 1 lines that form the hollow hourglass. A line has no spaces at its
# end.
#
# Constraints:
# - 1 <= n <= 20
#
# Example 1:
# Input:
# 4
#
# Output:
# *******
#  *   *
#   * *
#    *
#   * *
#  *   *
# *******
# Explanation: The first and last rows (k = 1) are 7 stars wide. Rows 2 and 3
# only have their two end stars. The middle row (k = 4 = n) has w = 1, so it
# is a single star with 3 leading spaces.
#
# Example 2:
# Input:
# 3
#
# Output:
# *****
#  * *
#   *
#  * *
# *****
# Explanation: For n = 3 there are 5 rows. The first and last rows have 5 stars,
# the second and fourth rows are * * with one leading space, and the middle row
# is a single star with 2 leading spaces.

# --- Solution using while loops ---

n = int(input())

# Build the sequence of row indices k: 1, 2, ..., n, n - 1, ..., 1
k_values = []
curr = 1
while curr <= n:
  k_values.append(curr)
  curr += 1

curr = n - 1
while curr >= 1:
  k_values.append(curr)
  curr -= 1

# Iterate through all 2n - 1 rows using a while loop
idx = 0
total_rows = len(k_values)
while idx < total_rows:
  k = k_values[idx]

  # 1. Leading spaces: k - 1 spaces
  spaces = ""
  s = 0
  while s < k - 1:
    spaces += " "
    s += 1

  # 2. Pattern width w = 2 * (n - k) + 1
  w = 2 * (n - k) + 1
  body = ""

  if k == 1 or k == n:
    # Full line of w stars
    cnt = 0
    while cnt < w:
      body += "*"
      cnt += 1
  else:
    # Star, (w - 2) spaces, then star (no trailing spaces)
    body += "*"
    inner_sp = 0
    while inner_sp < w - 2:
      body += " "
      inner_sp += 1
    body += "*"

  print(spaces + body)
  idx += 1