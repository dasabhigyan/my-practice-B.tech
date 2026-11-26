n = int(input())
arr = []
i = 0 
while i < n:
    arr.append(int(input()))
    i += 1
print(len(arr), arr[0], arr[-1])