'''         Part-9: Operator Preceedence:       '''
'''
1.**
2.<<>>
3.==  !=  <  >  <=  >=
4.not 
5.and
6.or 
'''


'''
<<>>(shifts)
& bitwise AND
^ bitwise XOR
| bitwise OR
* `== != ...` *(comparisons)*
'''
print(not 2 == 1) # here python sees it like not(2 == 1), here 2 == 1 is false and not of false is True. so the answer is true.
print((not 2) == 1) # here any non 0 number is True, so (not 2) is false, then false == 1 is also false. so the answer is false.
print()

print(3 << 1 + 1) # first 1+1 = 2 then shift the number by 2 that make the number 011 to 01100 which is 12
print((3 << 1) + 1) # first shifts the number make that 110 that is 6 and then add 1 becomes 7.
print()

print(12 & 10 == 8) # first bitwise operators works, which make the answer 8 and then 8 == 8, which becaomes True
print(12 & (10 == 8)) # first 10 == 8 becaomes false(0) then 12 & 0 ==> becomes 0
print()

