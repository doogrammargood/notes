str1 = "hi how are you?"
str2 = str1.split()[2]
print(str1==str2)
list1 = [1,2,3]
if len(str1)> len(str2):
    list1.append(3)
else:
    list1 = list1[::-1]
print(list1)