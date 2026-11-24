# Problem: Vertical Bar Chart
# Difficulty: HARD | Max Score: 75
#
# Draw a vertical bar chart. The first line of the input contains an integer k,
# the number of bars. The second line contains k integers, the heights of the
# bars from left to right.
# Let H be the largest height. Print the chart from the top level down to the
# bottom level: for each level r = H, H - 1, ..., 1 print one line of k
# characters. The character for a bar is '#' if the height of the bar is at
# least r, and '.' otherwise. Print nothing else.
#
# For the heights 3 1 4 1 5 the chart is:
# ....#
# ..#.#
# #.#.#
# #.#.#
# #####
#
# Input Format:
# - Line 1 contains k, the number of bars.
# - Line 2 contains k space-separated integers: the heights.
#
# Output Format:
# Print H lines of k characters each, from the highest level down to level 1,
# where H is the maximum height.
#
# Constraints:
# - 1 <= k <= 20
# - 0 <= every height <= 15
# - At least one height is 1 or more
#
# Example 1:
# Input:
# 5
# 3 1 4 1 5
#
# Output:
# ....#
# ..#.#
# #.#.#
# #.#.#
# #####
# Explanation: The largest height is 5, so there are 5 lines. Level 5 only has
# the bar of height 5. Level 4 has the bars of heights 4 and 5 (positions 3 and
# 5). Levels 3 and 2 have the bars of heights 3, 4 and 5 (positions 1, 3 and
# 5). Level 1 has all the bars.
#
# Example 2:
# Input:
# 4
# 0 2 0 1
#
# Output:
# .#..
# .#.#
# Explanation: The largest height is 2, so there are 2 lines. Level 2 has only
# the second bar (.#..). Level 1 has the second and the fourth bars (.#.#).
# The bars of height 0 stay empty.

# --- Solution using while loops ---

k = int(input())
parts = input().split()

# Parse k bar heights using a while loop
heights = []
idx = 0
while idx < k:
  heights.append(int(parts[idx]))
  idx += 1

# Find maximum height H using a while loop
max_h = heights[0]
m_idx = 1
while m_idx < len(heights):
  if heights[m_idx] > max_h:
    max_h = heights[m_idx]
  m_idx += 1

# Outer while loop iterates level r downward from max_h to 1
r = max_h
while r >= 1:
  line = ""
  # Inner while loop checks each bar j from 0 to k - 1
  j = 0
  while j < k:
    if heights[j] >= r:
      line += "#"
    else:
      line += "."
    j += 1

  print(line)
  r -= 1