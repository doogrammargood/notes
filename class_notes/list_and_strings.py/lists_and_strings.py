# #The purpose of this file is to give some examples of lists and strings.

#What we have seen so far:
print(0,"hello world") #"hello world" is a string. strings can be in single or double quotes.
print(1,type("hello world")) #this will tell us that "hello world" is a string.

'''
String slicing
'''
print(2,"hello world"[0]) #You can extract particular characters from a string using "slicing"
print(3,"hello world"[3])
print(4,"hello world"[6])

print("hello world"[10])
print("hello world"[-1])
x = "hello world"
print("last letter " ,x[len(x)-1])
print("first five letters ", "hello_world"[0:5])
print("last 5 letters", "hello_world"[-5:])

#String slicing format:
#"hello world"[first index(included; default 0): last index (excluded, default len()): step size (default 1)]

print("step size 2","hello world"[:])
'''
lists
'''
#lists are container objects that allow you to store variables for later access.
mylist = ['h',3,1,1,'0',"world"]
print(['h',3,1,1,'0',"world"])
print(type(mylist))

#lists can also be sliced.
print(mylist[2])

doubly_nested_list = [[1,3,5,7],[2,4,6,8]]
print(doubly_nested_list)