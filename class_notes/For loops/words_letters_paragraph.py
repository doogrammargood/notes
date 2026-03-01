paragraph = "A string like THIS ONE contains many words which themselves contain characters."

print(type(paragraph))

plist = paragraph.split()

print(paragraph)
print(type(plist))
print(plist)

def print_vowels_and_caps(x):
    for letter in x:
        if letter in 'aeiou': # won't match capital vowels
            print("vowel is: ", letter)
        if letter.isupper():
            print("Capital letter is: ", letter)

for word in plist:
    word1 = word.replace('.','')
    print("the word is: ", word1)
    print("This word length is: ", len(word1))
    print_vowels_and_caps(word1)