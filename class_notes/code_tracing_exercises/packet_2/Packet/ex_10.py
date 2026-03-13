def outer_function(x,num_times):
    def inner_function():
        print(x)
    for _ in range(num_times):
        inner_function()
outer_function("spam", 3)