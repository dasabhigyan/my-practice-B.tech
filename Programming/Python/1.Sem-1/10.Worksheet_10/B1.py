n = int(input())
i = 1
sum = 0 
while i <= n:
    a = int(input())
    sum += a
    i += 1
print(sum)


#----------------------------------------------------------------------------
n = int(input())
i = 1
arr = []
while i <= n:
    a = arr.append(int(input()))
    i += 1
b = sum(arr)
print(b)
