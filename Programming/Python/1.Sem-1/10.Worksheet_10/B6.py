n = int(input())

mat = []

a = 0

while a < n:
    l = list(map(int, input().split()))
    mat.append(l)
    a += 1

main_sum = 0
anti_sum = 0

a = 0
while a < n:
    main_sum += mat[a][a]
    anti_sum += mat[a][n - 1 - a]
    a += 1
print(main_sum, anti_sum)