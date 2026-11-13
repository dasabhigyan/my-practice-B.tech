# Read a single decimal value distance, representing the distance travelled in kilometres.
# 
# - If distance is 0, print:
#   No trip.
# 
# - If distance is greater than 0 and at most 2 km, the fare is a flat Rs.50. Print:
#   Fare: Rs.50.00
# 
# - If distance is greater than 2 km, the fare is Rs.50 plus Rs.15 for every kilometre beyond the first 2 km.
#   Print the fare with exactly two decimal places.
# 
# Input Format:
# Read one decimal number distance on a single line.
# 
# Output Format:
# Print exactly one line containing either the no-trip message or the calculated fare.

distance = float(input())
if distance > 0 and distance <= 2:
    print(f"Fare: Rs.{50:.2f}")
elif distance == 0:
    print("No trip.")
elif distance > 2:
    print(f"Fare: Rs.{(50 + (distance - 2)*15):.2f}")