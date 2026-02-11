#Computers are good at well-defined, repetitive tasks.
#For loops allow you to repeat the execution of code over and over.

my_list = [1,2,5,7,10,11,12] #A structure to loop through is called an "iterable"
# for x in my_list: #This defines a for loop.
#     print(x) #This line is repeated, as x ranges over the elements of my_list
#[print(x) for x in my_list] #This does exactly the same thing as our first loop.


# for y in my_list:
#     z= y%2
#     if z == 0: #you can put if block in a loop.
#         print(y)
#output_list=[print(y) for y in my_list if y%2==0] #This does exactly the same thing as the second loop.
#print(output_list)

# #--- for loops and list comprehensions ----#

# '''
# We have seen that list comprehensions 
# are a concise way of creating new list from old ones.

# List comprehensions and for loops are similar.
# '''


# #---Detect if a number is prime ---#
# p = 10 #We will show how to check if p is prime.
# p_is_prime = True #temporarily set to True
# for divisor_candidate in range(2,p):
#     if p % divisor_candidate==0: #if the divisor_candidate is actually a divisor of p...
#         p_is_prime = False
# print(f"{p_is_prime=}")

# #--- Is it possible to write a number as a sum of 3 squares?
# n = 143
# n_is_sum_of_3_squares = False
# for x in range(1,145):
#     for y in range(1,145):
#         for z in range(1,145):
#             if x**2 + y**2 + z**2 == n:
#                 print(x,y,z)
#                 n_is_sum_of_3_squares = True
# print(f"{n_is_sum_of_3_squares=}")

#--- Use loops to calculate the total cost of groceries.
grocery_costs = {'apple': 2, 'hotdogs': 5, 'spinach': 0.5, 'cheese': 1, 'bread':1.5} #keys are groceries, values are costs.
#print(grocery_costs['apple']+ grocery_costs['hotdogs']+grocery_costs['spinach']+grocery_costs['cheese'])
# running_total = 0
# for item in grocery_costs:
#     running_total += grocery_costs[item]
# print(running_total)
#print(sum([ grocery_costs[item] for item in grocery_costs]))
#--- Passwords ---#
for _ in range(3):
    user_input = input("enter your password")
    if user_input == "SecretPassword":
        print("access granted")
        break #breaks out of the loop
    else:
        print("incorrect password. Try again.")
        continue #continues in the loop

# #--- Loop through Dictionaries ----#
# my_dictionary = {'a': 1, 'b':2, 'c': 3}
# for key in my_dictionary:
#     print(key)
