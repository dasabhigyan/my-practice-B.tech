# Read two integers, one per line: score and attendance (both percentages).
# - If score is strictly greater than 90, print: Star student
# - If attendance is strictly greater than 90, print: Perfect attendance
# Both badges may be printed, one on each line, in that order.
# If neither condition holds, print exactly:
# No badges earned.
#
# Input Format:
# Two integers, one per line:
# - score
# - attendance
#
# Output Format:
# Print one or two badge lines, or a single line reading No badges earned. when neither badge is earned.


score = int(input())
attendance = int(input())
flag = False

if score > 90:
    print("Star student")
    flag = True
if attendance > 90:
    print("Perfect attendance")
    flag = True
if flag == False:
    print("No badges earned.")