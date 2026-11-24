"""
31. Hollow Square
----------------------------------------
Read an integer n and print a hollow square of n rows and n columns.
The cells on the border of the square (the first and last row, and the
first and last column) are '*', and all the cells inside are spaces (' ').

For n = 1, the square is a single '*'.
For n = 2, it is two lines of '**'.

Input Format:
- A single integer n.

Output Format:
- Print n lines of n characters each. No line has spaces after its last '*'.

Constraints:
- 1 <= n <= 20
- Time limit: 2000 ms | Memory: 256 MB
- Topic: Nested loop

Example 1:
Input:
5
Output:
*****
*   *
*   *
*   *
*****

Example 2:
Input:
3
Output:
***
* *
***
"""

n = int(input())

if n == 1:
    print("*")
elif n == 2:
    print("**")
    print("**")
else:
    print("*" * n)
    i = 1
    while i <= n - 2:
        print("*" + (" " * (n - 2)) + "*")
        i += 1
    print("*" * n)