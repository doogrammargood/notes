def count_double_letters(input_string:str)->int:
    '''Input: input_string is a string. We assume that it consists of only basic characters: lowercase letters, spaces and numbers.
    Output: The number of times a character is followed by itself.
    For example, when run on "raccoons appear, skiing weekly." it should output 5.
    When run on "hmmm...?", it should return 4.
    When run on "double  spaced  words", it should return 2.'''
    previous_letter=None
    counter = 0
    for letter in input_string:
        if letter == previous_letter:
            counter += 1
        else: #Note that this 'else' should not be here.
            counter -= 1
        previous_letter = letter
    return counter
print(count_double_letters("hmmm...?"))