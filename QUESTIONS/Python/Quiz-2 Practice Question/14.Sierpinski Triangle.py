# Problem: Sierpinski Triangle
# Difficulty: HARD | Max Score: 75
#
# Read an integer n and print n rows of a centred triangle. Row i (counting from
# 0) has n - 1 - i leading spaces, followed by i + 1 symbols separated by single
# spaces. The symbol number j (counting from 0) of row i is * if the entry
# C(i, j) of Pascal's triangle is odd, and . if it is even.
# Do not use a formula for C(i, j). Build each row from the previous row, as in
# Pascal's triangle, and keep only whether each number is odd or even (add the
# two numbers above and take the remainder after dividing by 2). The first and
# the last entry of every row are 1.
#
# Input Format:
# A single integer n.
#
# Output Format:
# Print n lines. A line has no spaces at its end.
#
# Constraints:
# - 1 <= n <= 32
#
# Example 1:
# Input:
# 4
#
# Output:
#    *
#   * *
#  * . *
# * * * *
# Explanation: Rows 0 and 1 of Pascal's triangle are 1 and 1 1, all odd, so
# they print * and * *. Row 2 is 1 2 1, and 2 is even, so it prints * . *.
# Row 3 is 1 3 3 1, all odd, so it prints * * * *.
#
# Example 2:
# Input:
# 8
#
# Output:
#        *
#       * *
#      * . *
#     * * * *
#    * . . . *
#   * * . . * *
#  * . * . * . *
# * * * * * * * *
# Explanation: For n = 8 the rows 0 to 7 of Pascal's triangle taken modulo 2
# give the Sierpinski pattern. Rows 3 and 7 are all stars, because 3 and 7 are
# one less than a power of 2.

# --- Solution using while loops ---

n = int(input())

# Store parity values (1 for odd, 0 for even) of the previous row in Pascal's triangle
prev_parity = []

i = 0
while i < n:
  curr_parity = []

  # Build row i of length i + 1 (indices j = 0 to i)
  j = 0
  while j <= i:
    if j == 0 or j == i:
      # First and last entry of every row are 1 (odd -> parity 1)
      curr_parity.append(1)
    else:
      # Sum of two numbers above mod 2 (keeps only odd=1 / even=0 parity)
      val = (prev_parity[j - 1] + prev_parity[j]) % 2
      curr_parity.append(val)
    j += 1

  # Leading spaces: n - 1 - i spaces
  spaces = ""
  s = 0
  while s < n - 1 - i:
    spaces += " "
    s += 1

  # Convert parity entries (1 -> '*', 0 -> '.') separated by single spaces
  symbols = []
  idx = 0
  while idx < len(curr_parity):
    if curr_parity[idx] == 1:
      symbols.append("*")
    else:
      symbols.append(".")
    idx += 1

  # Join symbols with single spaces so there is no trailing space at the end
  print(spaces + " ".join(symbols))

  prev_parity = curr_parity
  i += 1