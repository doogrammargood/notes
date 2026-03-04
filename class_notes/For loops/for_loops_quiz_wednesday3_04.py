str1 = "ABCDE"
str2 = "abcde"
str3 = "12345"
strings = [str1, str2, str3]
for index in range(5):
    print(index)
    for my_str in strings:
        print(my_str[index], end = '')
    print()
#What gets printed when the code is run?
