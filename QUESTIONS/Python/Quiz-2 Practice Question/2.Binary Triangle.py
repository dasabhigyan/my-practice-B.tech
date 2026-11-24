# Problem: Binary Triangle
# Difficulty: EASY | Max Score: 25
#
# Read an integer n. Print a triangle of n rows made of the digits 1 and 0.
# Row i has i digits, and the digits alternate between 1 and 0 along the row.
# A row with an odd number i starts with 1, and a row with an even number i
# starts with 0.
#
# Input Format:
# A single integer n.
#
# Output Format:
# Print n lines. Row i has i digits separated by single spaces, with no space
# at the end of the line.
#
# Constraints:
# 1 <= n <= 20
#
# Example 1:
# Input:
# 5
#
# Output:
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
#
# Example 2:
# Input:
# 3
#
# Output:
# 1
# 0 1
# 1 0 1

# --- Solution using while loops ---

n = int(input())

# Outer while loop iterates through each row i from 1 to n
i = 1
while i <= n:
  # Odd row starts with 1, even row starts with 0
  val = 1 if i % 2 == 1 else 0

  row = []
  # Inner while loop appends i alternating digits for the current row
  j = 0
  while j < i:
    row.append(str(val))
    val = 1 - val  # Toggle between 1 and 0
    j += 1

  # Join digits with single spaces and no trailing space at the end
  print(" ".join(row))
  i += 1