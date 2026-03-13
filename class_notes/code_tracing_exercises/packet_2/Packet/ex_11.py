def factory_function(x):
    def product_function(y):
        if x==0:
            return y
        else: 
            return y+1
    return product_function
for z in range(4):
    product_func = factory_function(z)
    print(product_func(z))