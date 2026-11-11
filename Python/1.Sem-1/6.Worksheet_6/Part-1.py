'''Part-1 List:The pointer Array'''
import sys
lst = []
for i in range(17):
    lst.append(i)
    print(f"len={len(lst):2d}  size={sys.getsizeof(lst)} bytes") 
print()
'''Here 2d = how many digit number. and getsizeof represents the data stored in it.
and .f in the make 
'''

print(sys.getsizeof([]))
print(sys.getsizeof([1]))
print(sys.getsizeof([1, 2]))
print(sys.getsizeof([1, 2, 3]))
print(sys.getsizeof([1, 2, 3, 4]))
print()

