# Read an integer n representing the total number of stones in the pile for the Nim Game.
# Determine and print whether the first player can win ("Win" or "Lose") assuming both players play optimally,
# where the first player can remove 1, 2, or 3 stones on each turn and the player who removes the last stone wins.
# 
# Input Format:
# A single integer n.
# 
# Output Format:
# "Win" if the first player has a winning strategy (n is not a multiple of 4), or "Lose" otherwise.




n = int(input())

# ── Write your solution here ──
if n % 4 == 0:
        print("Lose")
else:
        print("Win")