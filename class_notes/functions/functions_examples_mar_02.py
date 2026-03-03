#Functions and scopes
#In this file, we see some exotic behaviors that functions can adopt.

#--First example of a scoping problem--#

z=3
def example_function(x):
    '''
    Input: x is an integer.
    Output: x//2
    Side-effects: sets z=1
    '''
    global z #z now refers to the z outside of the function
    z=1
    return x//2
example_function(10)
#print(z) #Will z be 1 or 3?

#Key point: each function has its own 'scope' of variables that it can see. 
#By default, the z in example_function is different from the z outside of it.
#we can use the 'global' keyword to override this.
#Functions can view variables outside of their scope, but cannot modify them without the keywords global or nonlocal.

#--Example of a function that mutates its arguments.--#

def example_mutating_function(list_param):
    '''
    Input: list_param is a list. 
    Output: None
    Side-effects:?
    '''
    list_param[0]=50

my_list = [0,1,2,3]
example_mutating_function(my_list)
#print(my_list)

#Here is a first example of a higher-order function. Higher-order functions use functions as inputs or outputs to other functions.
#It is a function that returns a function.
#The function creates a counter.

def create_counter():
    '''
    Input: None
    Output: A function that increments a count each time it is called.
    Side-Effects: None
    '''
    count = 0
    def counter():
        '''
        Input: None
        Output: The current count
        Side-Effects: increments the count.
        '''
        nonlocal count
        count+=1
        return count
    
    return counter
counter_function1 = create_counter()
counter_function1()
counter_function1()
counter_function1()
print(counter_function1())
counter_function2 = create_counter()
counter_function2()
counter_function2()
print(counter_function2())
print(counter_function1())

#Here is another example of a higher-order function. This function constructs a linear function based on its slope and intercept.

def create_linear_function(a,b):
    '''
    Input: floats a and b.
    Output: The linear function that returns a*x+b on input x.
    Side-Effects: None
    '''
    def linear_function(x):
        '''
        Input: a float x
        Output: a*x+b, where a and b are defined in the enclosing scope.
        Side-Effects: None
        '''
        #nonlocal a,b
        return a*x+b
    return linear_function
f = create_linear_function(5,4)
#print(f(10))

#--Functions as arguments: Currying --#
def example_function_of_two_vars(x,y):
    return 2*x+y

def make_function_of_one_var(f,x):
    def function_to_return(y):
        return f(x,y)
    return function_to_return
my_func_of_one_var = make_function_of_one_var(example_function_of_two_vars, 10)
#print(my_func_of_one_var(2))

#--Arguments of unnumbered variables.--
def total(*args): #The star allows you to pass in unlimited arguments. The are stored as a tuple.
    print(type(args)) #says tuple
    to_return = 0
    for arg in args:
        to_return += arg
    return to_return
#print(total(10,16,5))