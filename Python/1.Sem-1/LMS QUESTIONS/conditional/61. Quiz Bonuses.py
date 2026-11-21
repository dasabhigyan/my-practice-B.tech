# Read three integer scores, one per line (each between 0 and 100).
# Check each of the following bonuses independently and print the matching line for every one that applies, in this order:
# - If any of the three scores equals 100, print: Perfect score bonus
# - If all three scores are strictly greater than 80, print: Consistency bonus
# - If the sum of the three scores is strictly greater than 250, print: High achiever bonus
#
# If none of the three bonuses apply, print exactly:
# No bonus earned.
#
# Input Format:
# Three integers, one per line.
#
# Output Format:
# Print one to three bonus lines, or a single line reading No bonus earned. when none apply.
a = int(input())
b = int(input())
c = int(input())
totalSum  = a + b + c
flag = False


if a == 100 or b == 100 or c == 100:
    print("Perfect score bonus")
    flag = True

if a > 80 and b > 80 and c > 80:
    print("Consistency bonus")
    flag = True

if totalSum > 250:
    print("High achiever bonus")
    flag = True

if flag == False:
    print("No bonus earned.")