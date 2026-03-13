def recursive_func(i,j):
    if i==0:
        return 1 + j
    else:
        return i*(recursive_func(i-1,j) + j)
print(recursive_func(3,0))
print(recursive_func(2,2))