puzzle = "Zpl4oNHpo6pSs78"
#loops
print(type(puzzle))
print(puzzle)
def find_secret(text):
    secret = ""
    message = ""
    for i in range(len(text)):
        if i % 2 == 0:   
            secret += text[i]
    for char in secret:
        if char.islower(): #True if its lowercase. Numbers are not lowercase.
            message += char
    return message
hidden_message = find_secret(puzzle)
print("The secret message is:", hidden_message)
#What gets printed?