# Read a single integer amount representing purchase amount in rupees.
# If amount is strictly greater than 1000, calculate a 10% discount and print:
# "Discounted price: Rs.X.XX" (rounded to 2 decimal places with comma thousands separators).
# If amount is 1000 or less, print: "No discount applied."
amount = int(input())
if amount > 1000:
        a = amount - amount*0.1

        print(f"Discounted price: Rs.{a:.2f}")
else:
        print("No discount applied.")