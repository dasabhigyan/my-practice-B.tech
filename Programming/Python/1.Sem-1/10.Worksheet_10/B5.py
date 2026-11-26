r, c = map(int, input().split())

mat = []

i = 0
while i < r:
    l = list(map(int, input().split()))
    mat.append(l)
    i += 1

# 1. -- This is Row Sum -- 
i = 0 
while i < r:
    j = 0 
    row_sum = 0 
    while j < c:
        row_sum += mat[i][j]
        j += 1
    print(row_sum, end = " ")
    i += 1
print()

# 2. -- This is for Column Sum --
j = 0 
while j < c:
    i = 0 
    col_sum = 0 
    while i < r:
        col_sum += mat[i][j]
        i += 1
    print(col_sum, end=" ")
    j += 1
