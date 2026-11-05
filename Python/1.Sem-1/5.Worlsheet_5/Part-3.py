'''             Part-3 Strings: Indexing, Slicing, Method and Tuples            '''
s = "Python"
print(s[0]) #P
print(s[1]) #y
print(s[-1]) #n
print(s[-2]) #o
print(s[3]) #h

#Slicing
s = "Programming"
print(s[3:7]) #gram
print(s[:4])    #Prog
print(s[4:] )    #ramming
print(s[-3:])    #ing
print(s[:-2])    #programm
print(s[:]  )   #programming
print()

print(s[::2] )   #pormig
print(s[::-1])   #gnimmargorP
print(s[1::2])   #rgamn
print()

text = "hello world"
print(len(text))    #11
print('o' in text)  #True
print('ow' in text) #False
print('xyz' in text)    #False
print('world' in text)  #True
print('World' in text)  #False
print()

s = "Hello World"
print(s.upper())    #HELLO WORLD
print(s.lower())    #hello world
print(s)    #Hello World 
print()

raw = "   hello world   "
print(raw.strip())     #Strips spaces from both sides 
print(raw.lstrip())     #Strip spaces from left side 
print(raw.rstrip())     #Strips spaces from right side 
print(len(raw), len(raw.strip()))   #17 and 11
print()

'''Important new concept to me'''
msg = "hello world"
print(msg.replace("world", "Python")) # replaces the (a,b) replace a from b, it will replace all a from b.
print(msg.replace("l", "L"))
print(msg)
print()

raw = "  HELLO, world!  "   
print(raw.strip().lower())  
print()

print(ord('A')) #65
print(ord('a')) #97 ord: Ordinal
print(ord('0')) #48
print(chr(65))  #A
print(chr(97))  #a chr: Character
print(chr(66))  #B
print()

print(chr(ord('A') + 3))    #D
print(chr(ord('z') - 25))   #a
print()

t = ("Alice", 95, True, 3.14)
print(t[0]) #Alice
print(t[-1])    #3.14
print(t[1:3])   #(95, True)
print(len(t))   #4
print()

# t[0] = "Bob"  # tuple is immutable.

print(type((1)))    #int
print(type((1,)))   # tuple
print()

