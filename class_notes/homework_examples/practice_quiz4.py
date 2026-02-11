'''Problem 1: Goal: Capitalize the zeroth letter of each word.
    Step 1: Use the split function to create a list of the words in the initial string.
    Step 2: Use a list comprehension, string addition, and the .captalize() function to capitalize the zeroth letter of each word.
    Step 3: Use the join function to recombine the words into a string.'''
initial_string: str = "Lorem ipsum dolor sit amet" #this is a shortened version of the homework's initial string.
init_string_after_step_1 = initial_string.split()
print(initial_string)
init_string_after_step_2 =[s.capitalize() for s in init_string_after_step_1 if 'e' in s] #This line has been changed
init_string_after_step_3 = " ".join(init_string_after_step_2)
string_with_each_word_capitalized = init_string_after_step_3
print(string_with_each_word_capitalized)