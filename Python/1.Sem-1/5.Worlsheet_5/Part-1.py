'''             Part-1:Lists,sets and Strings           '''
names = "Python"
scores = [95, 87, 92]
tags = {"Python", "AI", "Beginner"}
print(names[1])     # gives y as the Output
print(scores[1])        # 87 s the output
# print(tags[1])      # set is unorgainsed so it gives a type error. set is unordered
print()

print(type("hello"))        #class: str
print(type([1, 2, 3]))      #class: list
print(type({1, 2, 3}))      # class: set
print()

print(type({}))      # this dict
print(type(set()))   # this is a empty set
print()

# s = "hello"     # String is immutable data type so modyfing it rises error(here the error is TypeError)
# s[0] = "H"
# print(s)

lst = [10, 20, 30]      # List is mutable, so here the 0th index becomes 99
lst[0] = 99
print(lst)
print()

print({1, 2, 2, 3, 3, 3})   #here the output became {1,2,3} because set keep unique number in them 
print([1, 2, 2, 3, 3, 3])
print()

s = {1, 2, 3}
s.add(42)   # Works! 42 is an int (immutable)
s.add("hello")  # Works! "hello" is a str (immutable)
s.add((10, 20)) # Works! (10, 20) is a tuple of ints (immutable)
# s.add([1, 2]) # CRASHES! [1, 4] is a list (mutable) 
print(s)
print()

print('y' in "Python")  #True
print(87 in [95, 87, 92])   #True
print("AI" in {"Python", "AI", "Beginner"})     #True
print('z' in "Python")  #False
print(100 in [95, 87, 92])  #False
print("SQL" in {"Python", "AI", "Beginner"})    #False
print()

mixed = [42, "hello", True, 3.14, [1, 2, 3]]
print(len(mixed))   #Tell the length of the data-type 
print(type(mixed[0]))   #class: int 
print(type(mixed[1]))   #Class: str
print(type(mixed[4]))   #Class: list
print()

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[1][2]) #6
print(matrix[0][0]) #1
print(matrix[2][1]) #8
print()

article_tags = [
    {"Python", "AI"},
    {"Python", "Web"},
    {"AI", "ML"},
]
print(article_tags[0])  #{"Python", "AI"}
print("AI" in article_tags[1])  #False
print(len(article_tags))    #3
print()

data = [
    ("Alice", {95, 87, 92}),
    ("Bob",   {78, 85, 90}),
]
print(data[0][0])
print(data[1][1])
print(88 in data[0][1])
'''
Being **hashable** means a piece of data can never change, so Python can give it a permanent digital ID card to find it instantly in memory.
As a rule of thumb, immutable types like **numbers**, **strings**, and **pure tuples** are hashable, whereas mutable types 
like **lists**, **sets**, and **dictionaries**—or tuples containing mutable items—are unhashable because their contents can change
'''