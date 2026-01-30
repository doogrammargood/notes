'''We have seen so far:
Lists and Strings
    Slicing
    split/join
Today, we will see list comprehensions. They are easy ways of creating lists. 
                                        They are critical for manipulating data in Python.
'''
#Warm-up
x = "this is a string."
y = x.split()
z = "_".join(y)
print(z) #What gets printed?

#List comprehensions: first example
#List comprehensions allow you to create new lists by transforming existent lists. (They do not modify the existing list.)
L = [5,6,9,10]
#Suppose we want to double each element of L.
L_doubled = [2*x for x in L] #This is a list comprehension.

#List comprehensions: second example:
#We want to produce an acronym from a string. "The Art of Computer Programming" should become "T.A.O.C.P."
my_string = "The Art of Computer Programming"
words = my_string.split()
first_letters = [word[0] for word in words]
capitalized_first_letters = [l.capitalize() for l in first_letters]
print(".".join(capitalized_first_letters)+".")

#List comprehensions: third examples:
#Sequences of numbers defined by a formula
even_numbers = [2*n for n in range(10)] #note: range(10) behaves like the list [0,1,2,...,9]
square_numbers = [n**2 for n in range(10)]
reciprocals = [1/n for n in range(1,10)] #watch out for division by 0.

#if clauses: filtering
#Sometimes, we want to create a new list by removing some items from an existent list.

fruits=["apple","passionfruit","orange","bananna", "olive", "pear","grapefruit","tomato","jackfruit"]
fruits_that_end_in_fruit = [f for f in fruits if f[-5:]=="fruit"]

#Example