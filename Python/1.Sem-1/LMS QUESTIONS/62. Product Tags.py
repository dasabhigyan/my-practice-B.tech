# Read four integers, one per line: price, stock quantity, days since launch, and total units sold.
# Check each of the following conditions independently and print the matching tag on its own line for every condition that is true, in this order:
# - If price is less than 500, print: On sale
# - If stock quantity is less than 10, print: Low stock
# - If days since launch is less than 30, print: New arrival
# - If total units sold is greater than 1000, print: Bestseller
# 
# A product can match one to all four tags.
# If none of the four conditions hold, print exactly:
# No tags applicable.
#
# Input Format:
# Four integers, one per line:
# 1. price
# 2. quantity
# 3. days
# 4. units sold
#
# Output Format:
# Print one to four tag lines, or a single line reading No tags applicable. when none match.
price = int(input())
stockQuanity = int(input())
daysSinceLaunch = int(input())
totalUnitsSold = int(input())

tags = False

if price < 500:
    print("On sale")
    tags = True

if stockQuanity < 10:
    print("Low stock")
    tags = True

if daysSinceLaunch < 30:
    print("New arrival")
    tags = True

if totalUnitsSold > 1000:
    print("Bestseller")
    tags = True

if tags == False:
    print("No tags applicable.")