# Problem: Prime Triangle
# Difficulty: HARD | Max Score: 75
#
# Read an integer n and print a triangle of n rows that is filled with the
# prime numbers 2, 3, 5, 7, 11, ... in order. Row 1 has 1 prime, row 2 has the
# next 2 primes, row 3 has the next 3 primes, and so on: row i has i primes.
# The numbers of a row are separated by single spaces.
# Check whether a number is prime with a loop that tries the divisors.
#
# Input Format:
# A single integer n.
#
# Output Format:
# Print n lines. Row i has i primes, separated by single spaces.
#
# Constraints:
# - 1 <= n <= 12
#
# Example 1:
# Input:
# 4
#
# Output:
# 2
# 3 5
# 7 11 13
# 17 19 23 29
# Explanation: The primes in order are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29. Row 1
# takes 2, row 2 takes 3 and 5, row 3 takes 7, 11 and 13, and row 4 takes 17,
# 19, 23 and 29.
#
# Example 2:
# Input:
# 2
#
# Output:
# 2
# 3 5
# Explanation: Row 1 takes the first prime (2) and row 2 takes the next two
# primes (3 and 5).

# --- Solution using while loops ---

n = int(input())

candidate = 2  # Next integer to test for primality
row_num = 1    # Current row from 1 to n

# Outer while loop prints n rows
while row_num <= n:
  row_primes = []
  count_in_row = 0

  # Inner while loop collects 'row_num' prime numbers for the current row
  while count_in_row < row_num:
    # Check if 'candidate' is prime using a divisor loop
    is_prime = True
    if candidate < 2:
      is_prime = False
    else:
      divisor = 2
      while divisor * divisor <= candidate:
        if candidate % divisor == 0:
          is_prime = False
          break
        divisor += 1

    if is_prime:
      row_primes.append(str(candidate))
      count_in_row += 1

    candidate += 1

  # Print row primes separated by single spaces with no trailing space
  print(" ".join(row_primes))
  row_num += 1