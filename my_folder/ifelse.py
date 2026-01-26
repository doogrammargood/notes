num = input("enter a number:")
# num = int(num)
#print(num.isnumeric())

if num.isnumeric() and False:
    num = int(num)
    if num>0:
        print("positive")
    elif num<0:
        print("negative")
    else:
        print("zero")
else:
    print("not a number")
