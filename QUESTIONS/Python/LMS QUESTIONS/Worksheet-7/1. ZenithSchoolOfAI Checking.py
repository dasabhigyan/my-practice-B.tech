# Read a single lowercase letter c. 
# Print YES if c appears somewhere in the word "zenithschoolofai", and NO otherwise.
# 
# Input Format:
# One character.
# 
# Output Format:
# Exactly one line containing either YES or NO.

c = input().strip()

# ── Write your solution here ──
if c in "zenithschoolofai":
        print("YES")
else:
        print("NO")