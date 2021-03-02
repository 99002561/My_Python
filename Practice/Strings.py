course= "'python's course for Beginners"
course1= 'python course for "Beginners"'
course2='''
Hii Sai,
How are you?
'''
course='Python course for Beginners'
#SLICING
print(course[0]) #P
print(course[-1]) #s ,lly for -2=r
print(course[0:3]) #pyt( prints upto 3-1 )
# [0:] = Python course for Beginners
# [1:] = ython course for Beginners
# [:5] =pyth ,:5=0:5-1
print(course[:]) #Python course for Beginners
some=(course[:]) #copying the content
print(some) #Python course for Beginners
# Exercise
name='jennifer'
print(name[1:-1]) # prints from (m to n-1)