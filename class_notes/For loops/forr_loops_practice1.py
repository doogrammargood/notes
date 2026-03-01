paragraph = "A string like THIS ONE contains many words which themselves contain characters."

print(type(paragraph))

plist = paragraph.split()

print(paragraph)
print(type(plist))
print(plist)

for word in plist:
    word = word.replace('.','')
    print("the word is: ", word)
    print("This word length is: ", len(word))
    for letter in word:
        if letter in 'aeiou': # won't match capital vowels
            print("vowel is: ", letter)
        if letter.isupper():
            print("Capital letter is: ", letter)