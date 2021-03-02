# To find even or not
j = 14
print(10 & 1)  # if 0 it is even
'''
 00001110(14)       00001101(13)
 00000001(1)        00000001(1)
 00000000(even)     00000001(odd)
'''
# To find power of 2 or not
i = 32
if(i & (i-1)) == 0:
    print("It is power of 2")
'''
00100000(32)    00001001(9)
00011111(31)    00001000(8)
00000000(even)  00001000(odd number)
'''
# Program to print maximum number in a List
L = [5, 9, 4, 8, 6]
for i in L:
    if L[0] < i:
        L[0] = i
print(L[0])


# Program to print Reverse elements in the list
L = [1, 2, 3, 4, 5]
print(L)
A = len(L)
for i in reversed(range(1, A + 1)):
    a = i
    L.remove(i)
    L.append(a)
print(L)

# program to shift zeroes to right side
L = [1, 2, 3, 0, 4, 0, 5]
for i in L:
    if i == 0:
        L.remove(i)
        L.append(i)
print(L)


# Program to sum pair of numbers
L = [1, 4, 5, 3, 2, 6, 7]
A = len(L)
if A % 2 != 0:
    B = A//2
else:
    B = (A//2) + 1
for i in L:
    for x in range(0, B):
        if (L[x] + i) == 7:
            print(L[x], i)
