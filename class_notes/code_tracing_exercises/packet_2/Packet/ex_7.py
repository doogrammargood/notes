def calculate(x):
    total = 0
    for i in range(x):
        if i % 2 == 0:
            total = total + (i * 2)
        else:
            total = total + (i - 1)
    return total
print(calculate(3))
print(calculate(5))
