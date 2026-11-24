# Given a year Y, determine whether it is a leap year.
# A year is a leap year if:
#   - It is divisible by 4, AND
#   - It is not divisible by 100, UNLESS it is also divisible by 400.
#
# Input Format:
# A single line containing the integer year Y.
#
# Output Format:
# Print "Leap" if Y is a leap year; otherwise, print "Not Leap".
y = int(input())
if (y%4 == 0 and y%100 != 0) or y%400 == 0:
        print ("Leap")
else:
        print("Not Leap")