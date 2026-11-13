# Read a single integer score, representing a student's marks.
# Determine and print the student's distinction category based on the following rules:
# - If score is 85 or above, print: Distinction
# - Otherwise, print: No Distinction
#
# Input Format:
# Read one integer score on a single line.
#
# Output Format:
# Print exactly one line containing the respective distinction message.

units = int(input())
bill = 0 

if units <= 100:
        bill = units*1.5

elif units > 100:
        bill = units*2.5

print(f"Bill: Rs.{bill:.2f}")