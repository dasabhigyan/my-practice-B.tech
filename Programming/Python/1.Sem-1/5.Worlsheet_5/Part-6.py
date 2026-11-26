'''         Part-6 in/not in        '''
import time 
data_list = list(range(1_000_000)) #list of 1 million number numbers(0 to 999,999)
data_set  = set(range(1_000_000))   # set if 1 million numbers(0 to 999,999) 
target    = 999_999 # we neet to cearch for this number 
t0 = time.time() #saves current time 
_ = target in data_list #Linear search through 1 million items || Underscores '_'make large numbers readable || amd ',' commas will make the inputs as a  tuple
print(f"list: {(time.time() - t0)*1000:.3f} ms")
t0 = time.time() 
_ = target in data_set  # Instant hash lookup
print(f"set:  {(time.time() - t0)*1000:.6f} ms") # here 1st it captures the time and the substract it from the previous time saved.
print()

""" ===================================================================
 CONTAINER TRADE-OFF TABLE (Q29) 
 ===================================================================
   | Property           | list | set | str | 
   |-----------------------------|-------|-------|-------| 
   | in time complexity  | O(N) | O(1) | O(N) | 
   | Ordered (indexable) | Yes | No | Yes | 
   | Allows duplicates   | Yes | No | Yes | 
   | Mutable             | Yes | Yes | No | 
   | Elements must be hashable | No | Yes | N/A |
 =================================================================== """

