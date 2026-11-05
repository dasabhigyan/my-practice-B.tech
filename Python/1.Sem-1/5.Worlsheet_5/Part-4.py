'''             Part-4 Lists:Indexing,Slicing,Slicing & Mutation            '''
# lst = [10, 20, 30, 40, 50]
# print(lst[0])   # 10
# print(lst[-1])  # 50
# print(lst[1:3]) # [20, 30]
# print(lst[::-1]) # [50, 40, 30, 20, 10]
# lst[2] = 99 
# print(lst) # [10, 20, 99, 40, 50]
# print()

# lst = [10, 20, 30]
# lst.append(40) # lst = [10, 20, 30, 40]
# lst.append(50)  # lst = [10, 20, 30, 40, 50]
# print(lst)
# print()

# lst = [10, 20, 30, 40, 50]
# x = lst.pop() # removes the last element from the list
# print(x) #prints the removed elements.
# print(lst)  #[10, 20, 30, 40]
# y = lst.pop(1)  #removes the indexed value
# print(y)    #20
# print(lst)  # [10, 30, 40]
# print()

# lst = [10, 20, 30, 20, 40]
# lst.remove(20)  # remove the value from the list, remove the 1st occrance of the same value.
# print(lst)   #[10, 30, 20, 40]
# lst.remove(99)  # ValueError

nums = [3, 1, 4, 1, 5, 9, 2]
new = sorted(nums)  
print(new) #[1, 1, 2, 3, 4, 5, 9]
print(nums) #[3, 1, 4, 1, 5, 9, 2]
nums.sort()
print(nums) #[1, 1, 2, 3, 4, 5, 9]
print()

