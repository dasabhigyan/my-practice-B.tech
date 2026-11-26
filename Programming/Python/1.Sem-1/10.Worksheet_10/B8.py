r, c = map(int, input().split())

mat = []

i = 0

while i < r:
    l = list(map(int, input().split()))
    mat.append(l)
    i += 1

#--------------------------------------------------------

d = 0
while d < r + c - 1:
    i = 0 
    while i < 2:
        j = d - 1
        if 0 <= j < c:
            print(mat[i][j], end = " ")
        i += 1
    d += 1
