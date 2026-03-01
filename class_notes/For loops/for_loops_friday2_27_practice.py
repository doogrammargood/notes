word = "TULANE"
rows = 3
for r in range(1, rows + 1):
    for c in range(len(word)):
        char = word[c]
        if r == (c % rows) + 1:
            print(char, end=" ")
        else:
            print("-", end=" ")
    print()

#What is the output? 