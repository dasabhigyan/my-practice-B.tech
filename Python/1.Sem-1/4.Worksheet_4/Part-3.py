'''                 Part-3 Combination Condition                '''
score = 55
attendance = 80
print(score >= 40 and attendance >= 75) #True as in AND both the condition is True so here the output is true.
print()

print(True and False) #False
print(True or False) #True 
print(not True) #False
print((5 > 3) and (2 > 4)) #False
print()

print(bool(0), bool(0.0), bool(""), bool(None)) #False False False False (In the 3rd "" is false where as " " is True)
print(bool(5), bool("hi"), bool(-1)) #True True True (anything except 0 is True)
print()

print(0 or 5) #5
print("" or "hi") #hi
print(3 and 7)  #7 (in AND when the output is True, the output is the last Truthy value.)
print(0 and 7) #0 (in AND when the output is False, the outpu tis the 1st Falsy Value.)
print()

name = ""
print(name or "Guest") #Guest
name = "Asha"
print(name or "Guest") #Asha (in OR when the output is True, the output is 1st Truthy Value.)
print()

print(True or False and False) #True
'''
The order is not>and>or
so here 1st false and false which is false the true and false which os TRUE.
'''
