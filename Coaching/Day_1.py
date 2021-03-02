# Printing Statements
print("welcome")
# Data types
i = 10
print(type(i))
i = 10.2
print(type(i))
i = "text"  # or i = 'text'
print(type(i))
# Operators
# Operator Precedence -> (),*,+,-
# Arithmetic -> +,-,/,*,//,**,%
print(2 ** 3)  # 2*2*2 = 8
print(10 / 3)  # (10.0/3.0) ->float division
print(10 // 3)  # (10/3) -> integer division
# Relational -> ==,!=,<,<=,>,>=
print(10 < 20)  # True
print(10 == 10)
print(10 >= 20)
# Logical -> and, or,not
print((10 < 20) and (10 > 5))  # True
print((10 < 20) or (10 > 5))
print(not 10 < 20)  # not true is FALSE
# Bitwise -> &,|,~,^,<<,>>
print(10 & 14)
'''
 00001010(10)
 00001110(14)
 00001010(10)
 '''
print(10 | 14)
print(60 << 2)  # 00111100 << 2 = 11110000 (left shift)
print(60 >> 2)  # 00111100 >> 2 = 00001111 (right shift)
'''
# Interpreter + compiler proof
print('start')
i = 10
j = i + k # Semantic error
j = i +    # syntax error
print(j)
print(end)
'''
# int,str,float are immutable(not modifiable)
i = 10
print(i)
print(id(i))  # prints unique id of the variable
i = i + 10
print(i)
print(id(i))  # 1st address will be garbage

# Strings
Text = "Python Programming"  # index starts from 0 to n(+ve index) or -n to -1(-ve index0
Text1 = " By me"
print(id(Text1))
Text1 = Text + Text1
print(Text1)  # addition can be done for integers / strings but not for int + str
print(id(Text1))  # 1 id of Text1 will be garbage(removed)
print(Text)  # same as print(Text[:]), print(Text[0:]), print([::])
print(Text[5])  # prints 5th index value
#  Positive Slicing
print(Text[5:10])  # to print substring from index 5 to index (10-1)
# Stepping
print(Text[0:15:2])  # Prints 0,2,4,6,8,10,12,14
# Negative Slicing
print(Text[-1])
print(Text[-1:-10])  # prints nothing because step is not included
print(Text[:-10:-1])  # prints -1 to -9
# To reverse a string
print(Text[-1:-19:-1])
print(Text[::-1])
print(Text[-1::-1])
# Combing +ve and -ve slicing
print(Text[0:-10])  # Same as print(Text[:-10]) Python P (-10 i from negative end)
print(Text[0:8])  # Same as above , print(Text[:8])

T = 'sai'
T1 = ' kumar'
T1 = T + T1
print(T1)
'''
T1[1] = 'A'  # string can't be modified
print(T1)
'''
# To print Sai\Kumar, \ is a meta character ,to disable use one more \ i.e, \\
print("Sai\\kumar")
print("a\\b")  # a\b
print("a\\\\b")  # a\\b
# Escape sequences \n - new line, \t - tab space

# string methods
A = 'Sai Kumar'
print(len(A))

B = '  sai Kumar  '
print("===" + B + "===")
C = B.strip()
print("===" + C + "===")
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)
a = '...ss..sai...'
b = a.strip('.s')
print(b)
Txt = 'C,C++,Java,Python'
a = Txt.split(',')  # ['C', 'C++', 'Java', 'Python']
print(a)
a = Txt.split()  # ['C,C++,Java,Python']
print(a)
N = "Saikuimair"
b = N.split('i')
print(b)

te = 'sai'
print(te.startswith('s'))
print(te.startswith('a'))

te = 'sai'
print(te.endswith('i'))
print(te.endswith('a'))

te = 'sAi'
print(te.upper())

te = 'SAi'
print(te.lower())

