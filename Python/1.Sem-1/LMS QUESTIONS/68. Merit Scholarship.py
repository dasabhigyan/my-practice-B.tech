# Read a single integer score out of a maximum of 150 marks.
# Calculate percentage = (score / 150) * 100.
# If percentage is 90% or above, print: "Merit scholarship awarded. Percentage: X.XX%"
# If percentage is below 90%, print: "Not eligible for merit scholarship. Percentage: X.XX%"
# The percentage must always be displayed with two decimal places.
score = int(input())
percentage = (score/150)*100
if percentage >= 90:
        print(f"Merit scholarship awarded. Percentage: {percentage:.2f}%")
else:
        print(f"Not eligible for merit scholarship. Percentage: {percentage:.2f}%")