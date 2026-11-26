r, c = map(int, input().split())

mat = []

i = 0 

while i < r:
    l = list(map(int, input().split()))
    mat.append(l)
    i += 1

#-----------------------------------
j = 0
while j < c:
    i = 0
    while i < r:
        print(mat[i][j], end = " ")
        i += 1
    print()
    j += 1
