'''     Part-6 The Language of Bits:The Binary Numbers          '''
print(bin(13))      #0b1101
'''
16  8   4   2   1
0   1   1   0   1
'''
print(bin(255))     #0b11111111
print()

print(int("1010", 2)) #10
print(int("11111", 2)) #31
print()

print(bin(42))          # base 2    0b101010
print(oct(42))          # base 8    0o52
print(hex(42))          # base 16   0x2a
print(int("101010", 2)) # binary string -> decimal  42
print(int("52", 8))     # octal string  -> decimal  42
print(int("2a", 16))    # hex string    -> decimal  42
print()

print(0b101010)   # binary literal  42
print(0o52)       # octal literal   42
print(0x2a)       # hex literal 42
print()

