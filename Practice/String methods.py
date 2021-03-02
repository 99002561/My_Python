course = 'Python for Begginers'
print(len(course)) #20 ,print and len are not specified to any objects ,it is general purpose function
#SPECIFIC FUNCTIONS
print(course.upper()) #When a function is specific to object(strings)it is method.
print(course) #not modified
print(course.lower())
print(course.find('P')) #0 ,lly for 'o' ans is 4
#find is a case sensitive and returns index

print(course.find('Begginers')) # B starts at 11
print(course.replace('Begginers', 'Absolute Beginners')) #Python for Absolute Beginners
print(course.replace('begginers', 'Absolute Beginners'))#Python for Begginers
print(course.replace('P','J')) #Jython for Begginers
print('Python' in course) #True ,in returns boolean
print('Python' not in course) #False
