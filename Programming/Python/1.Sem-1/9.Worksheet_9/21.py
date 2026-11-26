i = 1
while i <= 4:
    j = 1
    while j <= 4:
        if (i*j)%2 ==0 :
            print("E", end = " ")
        else:
            print("O", end = " ")
        j += 1
    print()
    i += 1
