print(19 // 7) #2
print(100 // 7) #14
print(8 // 0) #ZeroDivisionError

print(int(-19 / 7)) #-2
print(-19 // 7) # -3 (The output of // towards left so the answer is -3.)

print( 19 //  7) # 2 (This is because the division is 2.71 but it floats toward left so the answer is 2)
print(-19 // -7) # 2
print(-19 //  7) # -3 (This is because the division is -2.71 but it floats toward left so the answer is -3)
print( 19 // -7) # -3

print(-19 % 7) #-3
print(19 % -7) #-3
print(19 / -7, 19 % -7, 19 // -7) #-2.71 -2 -3 (in modulo(%) the output is -2 instead of -5 because in negative the answer to the right of the output code.)

#  rem = x - int(x/y)*y . Test it against Python's  %  for a negative
x, y = -19, 7
print(x - int(x/y) * y)
print(x % y)

