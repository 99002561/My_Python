# Python offers hash() method to encode the data into unrecognisable value.
# Hash method in Python is a module that is used to return the hash value of an object.
a = 150.5
print(hash(a))
b = ('a', 'e', 'i', 'o', 'u')  # tuples are immutable(can't change)
print(hash(b))
c = ['a', 'e', 'i', 'o', 'u']  # lists are mutable
#print(hash(c))  # hash() returns hashed value only for immutable objects
b = 150.5
print(hash(b))
if hash(a) == hash(b):
    print('Yes')
