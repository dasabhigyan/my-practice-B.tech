''' Part-3: Set:The Has'''
#hash() in python 
print(hash(42))
print(hash(42))           # run again
print(hash(3.14))
print(hash((1, 2, 3)))    # tuple: hashable

'''Those numbers are the unique numeric fingerprints Python calculates for each value to place and find it instantly in memory, which works because integers, floats, and tuples are all frozen (immutable).'''

print(hash([1, 2, 3]))    # list: predict crash or value?