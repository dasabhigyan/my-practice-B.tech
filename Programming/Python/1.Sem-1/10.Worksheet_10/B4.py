r, c = map(int, input().split())

mat = []

i = 0 
while i < r:
    l = list(map(int, input().split()))
    mat.append(l)
    i += 1

#--- Next step: walk mat[i][j] and sum all cells --- 
total = 0
while i < r:
    j = 0 
    while j < c:
        total += mat[i][j]
        j += 1
    i += 1
print(total)