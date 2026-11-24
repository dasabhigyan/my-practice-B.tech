# Problem: Max Number Grid
# Difficulty: EASY | Max Score: 25
#
# Read an integer n. Print an n x n grid of numbers. The number in row i and
# column j (both counted from 1) is the larger of i and j.
#
# Input Format:
# A single integer n.
#
# Output Format:
# Print n lines. Each line has n numbers separated by single spaces, with no
# space at the end of the line.
#
# Constraints:
# - 1 <= n <= 15
#
# Example 1:
# Input:
# 4
#
# Output:
# 1 2 3 4
# 2 2 3 4
# 3 3 3 4
# 4 4 4 4
# Explanation: Row 1 is 1 2 3 4 (the larger of 1 and j is j). Row 2 is 2 2 3 4,
# row 3 is 3 3 3 4 and row 4 is 4 4 4 4.
#
# Example 2:
# Input:
# 2
#
# Output:
# 1 2
# 2 2
# Explanation: Row 1 is 1 2 and row 2 is 2 2.

# --- Solution using while loops ---

n = int(input())

# Outer while loop iterates through row i from 1 to n (1-based indexing)
i = 1
while i <= n:
  row_items = []
  # Inner while loop iterates through column j from 1 to n (1-based indexing)
  j = 1
  while j <= n:
    # Value at (i, j) is the larger of i and j
    val = i if i >= j else j
    row_items.append(str(val))
    j += 1

  # Join numbers with single spaces and no trailing space at the end
  print(" ".join(row_items))
  i += 1