# Read a single integer score between 0 and 100.
# Print a single letter grade based on the score using this scale:
# - 90 and above → A
# - 80–89 → B
# - 70–79 → C
# - 60–69 → D
# - Below 60 → F
#
# Input Format:
# One integer score on a single line.
#
# Output Format:
# Exactly one line containing the letter grade.
score = int(input())

if score >= 90:
        print("A")
elif score >=80 and score < 90:
        print("B")
elif score >= 70 and score < 80:
        print("C")
elif score >= 60 and score < 70:
        print("D")
else:
        print("F")