i = 1
while i <= 3:
    j = 1
    while j <= 3:
        if j <= i:
            print("#", end = "")
        else:
            print(".", end ="")
        j += 1 
    k = 1 
    while k <= 3:
        if k > i:
            print("#", end = "")
        else:
            print(".", end = "")
        k += 1 
    print()
    i += 1