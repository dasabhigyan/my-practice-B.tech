parts = input().split()
arr = []
i = 0 
while i < len(parts[i]):
    arr.append(int(parts[i]))
    i += 1

largest = arr 
smallest = arr 
i = 1 
while i < len(arr):
    if arr[i] > largest:
        largest = arr[i]
    if arr[i] < smallest:
        smallest = arr[i]
    i += 1
print(largest, smallest)