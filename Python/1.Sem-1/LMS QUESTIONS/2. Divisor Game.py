# Read an integer n representing the starting number for the Divisor Game.
# Determine and print the winner ("Alice" or "Bob") assuming both players play optimally.
# Alice wins if n is even, and Bob wins if n is odd.
# 
# Input Format:
# A single integer n.
# 
# Output Format:
# "Alice" or "Bob" depending on who wins the game.



n = int(input())

# ── Write your solution here ──
if n%2 == 0:
        print("Alice")
else:
        print("Bob")
    