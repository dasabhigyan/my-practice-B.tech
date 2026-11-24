# Problem: Alphabet Pyramid
# Difficulty: MEDIUM | Max Score: 50
#
# Read an integer n. Print a centred pyramid of n rows made of capital letters.
# Row i has n - i leading spaces, then the letters A, B, C, ... up to the i-th
# letter of the alphabet, and then the letters go back down to A.
# There are no spaces between the letters.
#
# Input Format:
# A single integer n.
#
# Output Format:
# Print n lines. Row i has n - i leading spaces and 2i - 1 letters.
#
# Constraints:
# 1 <= n <= 26
#
# Example 1:
# Input:
# 4
#
# Output:
#    A
#   ABA
#  ABCBA
# ABCDCBA
#
# Example 2:
# Input:
# 6
#
# Output:
#      A
#     ABA
#    ABCBA
#   ABCDCBA
#  ABCDEDCBA
# ABCDEFEDCBA

# --- Solution using while loops ---

n = int(input())

# Outer while loop iterates through each row i from 1 to n
i = 1
while i <= n:
  # Compute leading spaces for centering row i
  spaces = " " * (n - i)

  # Inner while loop builds ascending letters from 'A' to the i-th letter
  asc = ""
  j = 0
  while j < i:
    asc += chr(ord("A") + j)
    j += 1

  # Inner while loop builds descending letters from (i - 1)-th letter down to 'A'
  desc = ""
  k = i - 2
  while k >= 0:
    desc += chr(ord("A") + k)
    k -= 1

  # Print the complete row without extra spaces between letters
  print(spaces + asc + desc)
  i += 1