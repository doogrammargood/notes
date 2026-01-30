#Checking string equality
print(1,"Hi"=="Hi")
print(2,"Hi"=="hi")
#print(3,"Hi"="hi") #We need ==
x = "str_name"
y = "str_name"
print(3, x==y) #Checks if x and y have the same value
#print(4, x is y) #Checks if x and y are the same object.

print(3.1, ['a','b']==['a','b'])
print(3.2, ['a','b']==['b','a'])

print(3.3,['a','b'] is ['a','b']) #is checks whether the two objects are literally the same.

#String containment: 
x="hello"
y="ll"
print(4,y in x)
print(5, "eo" in "hello")

print(6,'a' in ['a','b'])
print(7, 'c' in ['a','b'])

#addition
x="my_string"
y="thread"
print(8,x+y) #adding strings concatenates them.

print(9, x + "") #adding the emptystring doesn't change the string.

x=['a',1,3]
y=['x']
print(10,x+y) #adding lists concatenates them.
print(11, x+[])

#--String methods: Join and Split
x="This is my sentence."
z=x.split()
print(12,x.split())
y="This is one sentence. This is another sentence. And a third."
print(13, y.split('.'))

print(14, "".join(z))
print(15, "-".join(z))
#---Nested lists
x = [[1,2],[3,4,5]]
print(16,len(x))
print(17,len(x[1]))

#---Appending to a list
x.append('x')
print(18,x)
print(19,x.append('z'))
print(x)


