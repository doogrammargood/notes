def my_function(a,b=0):
    '''
    Input: an integer
    Output: is None
    Side-effects: Prints the next even number.
    Note: This function serves as an example. No practical use.
    '''
    if a%2==0:
        print(a)
    else:
        print(a+1)
    print(b)
# print(1)
# x=my_function(5,b=7)
# y=my_function(6,b=8)
# print(x)
# print(y)
def function_calling_function():
    my_function(8)

function_calling_function()