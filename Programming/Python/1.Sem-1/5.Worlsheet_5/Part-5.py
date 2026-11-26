'''         Part-65Sets: Operations & Why No Indexing           '''
s = {"Alice", "Bob", "Charlie"}
s.add("Dana")
print(s)
s.add("Zara")
print(s)
s.discard("Alice")  #discard will not crash the program if the element is not founf, the program will c
print(s)
# s.discard("Zara")
# print(s)
s.remove("Zara")      # remove will crash the program if the element is not found.
print(s)
print()

python_devs = {"Alice", "Bob", "Charlie", "Dana"}
ml_devs     = {"Bob", "Dana", "Eve", "Frank"}

print(python_devs | ml_devs)    #prints all names in both the sets.(union)

print(python_devs & ml_devs)    #only prints that name which is common on both(intersection)

print(python_devs - ml_devs)    # just like mathemtical set({'Alice', 'Charlie'})

print(ml_devs - python_devs)    #{'Eve', 'Frank'}

print()

print(python_devs.union(ml_devs))   #{'Dana', 'Bob', 'Eve', 'Frank', 'Charlie', 'Alice'}
print(python_devs.intersection(ml_devs))    #{'Dana', 'Bob'}
print(python_devs.difference(ml_devs))      #{'Alice', 'Charlie'}

