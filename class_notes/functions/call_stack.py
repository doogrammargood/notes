import inspect

def print_call_stack():
    stack = inspect.stack()
    
    # Skip the current function (print_call_stack itself)
    functions = [frame.function for frame in stack[1:]]
    
    # Reverse so it prints from outermost → innermost
    for name in reversed(functions):
        print(name)

def my_function():
    print_call_stack()

def my_outer_function():
    my_function()

my_outer_function()