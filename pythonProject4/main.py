'''
L = [1, 2, 3, 4, 5]
for i in L:
    if L[0] < i:
        L[0] = i
print(L[0])
'''
'''
L = [1, 3, 0, 0, 5, 7, 0, 9]
for i in L:
    if i == 0:
        L.remove(i)
        L.append(0)
print(L)
'''

L = [1, 4, 5, 3, 2, 6, 7]
A = len(L)
if A % 2 == 0:
    B = (A // 2)
else:
    B = (A // 2) + 1
for i in L:
    for x in range(1, B):
        if L[x - 1] + i == 7:
            print(L[x - 1], i)
