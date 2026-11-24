# Problem: Number Diamond
# Difficulty: MEDIUM | Max Score: 50
#
# Read an integer n. Print a diamond of numbers made of 2n - 1 rows. The rows
# are numbered i = 1, 2, ..., n and then i = n - 1, n - 2, ..., 1. Row i is
# made of:
# 1. 2 * (n - i) spaces at the start
# 2. then the numbers 1 2 3 ... i ... 3 2 1 (they go up to i and then come
#    back down to 1), separated by single spaces
#
# Input Format:
# A single integer n.
#
# Output Format:
# Print the 2n - 1 rows of the diamond. Rows have no spaces at the end.
#
# Constraints:
# - 1 <= n <= 15
#
# Example 1:
# Input:
# 3
#
# Output:
#     1
#   1 2 1
# 1 2 3 2 1
#   1 2 1
#     1
# Explanation: n = 3. The rows are i = 1, 2, 3, 2, 1. Row 1 has 4 leading spaces
# and the number 1. Row 2 has 2 leading spaces and 1 2 1. Row 3 has no leading
# space and 1 2 3 2 1. Then the rows i = 2 and i = 1 are printed again.
#
# Example 2:
# Input:
# 4
#
# Output:
#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1
#   1 2 3 2 1
#     1 2 1
#       1
# Explanation: n = 4. The rows are i = 1, 2, 3, 4, 3, 2, 1. Row 1 has 6
# leading spaces, row 2 has 4, row 3 has 2 and row 4 has none (1 2 3 4 3 2 1).

# --- Solution using while loops ---

n = int(input())

# Build sequence of row values i: 1, 2, ..., n, n - 1, ..., 1
row_vals = []
curr = 1
while curr <= n:
  row_vals.append(curr)
  curr += 1

curr = n - 1
while curr >= 1:
  row_vals.append(curr)
  curr -= 1

# Iterate through all 2n - 1 rows using a while loop
idx = 0
total_rows = len(row_vals)
while idx < total_rows:
  i = row_vals[idx]

  # 1. Leading spaces: 2 * (n - i) spaces
  leading_spaces = ""
  s = 0
  while s < 2 * (n - i):
    leading_spaces += " "
    s += 1

  # 2. Build single-space-separated sequence: 1 2 ... i ... 2 1
  nums = []

  asc = 1
  while asc <= i:
    nums.append(str(asc))
    asc += 1

  desc = i - 1
  while desc >= 1:
    nums.append(str(desc))
    desc -= 1

  # Join numbers with single spaces so there are no trailing spaces
  print(leading_spaces + " ".join(nums))
  idx += 1