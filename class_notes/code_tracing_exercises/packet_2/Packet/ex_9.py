def add(a,b):
    return a+b
def mul(a,b):
    return a*b
a, b, c = 5, 9, 3
d = add(mul(a,b), mul(a,c))
e = mul(a,add(b,c))
print(d==e)