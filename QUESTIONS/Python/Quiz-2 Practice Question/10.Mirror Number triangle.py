# Problem: Mirror Number Triangle
# Difficulty: MEDIUM | Max Score: 50
#
# Read an integer n. Print n rows. Row i (counting from 1) is made of three
# parts written next to each other, with nothing else in between:
# 1. the numbers 1, 2, ..., i written one after the other with no spaces
# 2. then 2 * (n - i) spaces
# 3. then the numbers i, i - 1, ..., 1 written one after the other with no spaces
#
# Input Format:
# A single integer n.
#
# Output Format:
# Print n rows as described above. Rows have no spaces at the end. The numbers
# are written without any space between them (so 10 is written as the two
# characters 1 and 0).
#
# Constraints:
# - 1 <= n <= 15
#
# Example 1:
# Input:
# 4
#
# Output:
# 1      1
# 12    21
# 123  321
# 12344321
# Explanation: n = 4. Row 1 is 1, then 6 spaces, then 1. Row 2 is 12, then 4
# spaces, then 21. Row 3 is 123, then 2 spaces, then 321. Row 4 has no space
# in the middle: 1234 followed by 4321.
#
# Example 2:
# Input:
# 3
#
# Output:
# 1    1
# 12  21
# 123321
# Explanation: n = 3. Row 1 is 1, 4 spaces, 1. Row 2 is 12, 2 spaces, 21. Row 3
# is 123 followed by 321.

# --- Solution using while loops ---

n = int(input())

# Outer while loop iterates through row i from 1 to n
i = 1
while i <= n:
  # 1. Ascending numbers: 1, 2, ..., i with no spaces
  left_part = ""
  a = 1
  while a <= i:
    left_part += str(a)
    a += 1

  # 2. Middle spaces: 2 * (n - i) spaces
  mid_spaces = ""
  sp = 0
  while sp < 2 * (n - i):
    mid_spaces += " "
    sp += 1

  # 3. Descending numbers: i, i - 1, ..., 1 with no spaces
  right_part = ""
  d = i
  while d >= 1:
    right_part += str(d)
    d -= 1

  print(left_part + mid_spaces + right_part)
  i += 1