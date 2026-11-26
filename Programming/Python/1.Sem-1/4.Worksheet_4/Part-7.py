'''         Bitwise Operator            '''
# & this is AND Operator.
print(13 & 10)      #8
print()
print(bin(13))
print(bin(10))
print(bin(13 & 10))
'''
1101
1010
+----
1000 (int 8)
'''
print()
print(12 & 10)
'''
1100
1010
+---
1000 (int 8)
'''
print(6 & 3)
'''
0110
0011
+---
0010 (int 2)
'''

# | this is OR operator
print(12 | 10)
'''
12-1100
10-1010
+------
14-1110
'''
print()

# ^ This is XOR Operator.(if both the value are same then its FALSE, and if both the value are differet the the value is TRUE)
print(12 ^ 10)
'''
1100
1010
+---
0110 (int 6)
'''
print()
#Shifts - << abd >>
'''<<  shifts all bits left by n positions (fills with 0 on the right);  >>  shifts right.'''
print(bin(3))       # 0b11
print(bin(3 << 1))  # shift left 1
print(bin(3 << 2))  # shift left 2
print(bin(3 << 3))  # shift left 3
print()

print(5 and 3) #3 If the expression is true, the last truthy value returns.
print(5 & 3) #1
print(5 or 3) #5 If the expression is tue the 1st truthy value returns.
print(5 | 3) #7

#Odd/even check:
print(7 & 1)    #if the output is 1 then the output is odd.
print(8 & 1)    # if the output is 0 then the output is even.
print()

#Bits flags - permission in one integer:
READ    = 0b100   # 4
WRITE   = 0b010   # 2
EXECUTE = 0b001   # 1
perms = READ | WRITE   # user can read and write, but not execute
print(bin(perms))      # prints 110 as the output 
print(bool(perms & READ))      # can the user read?     100 which is True 
print(bool(perms & EXECUTE))   # can the user execute?  000 which is False 
print()

