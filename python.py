introString = input("Enter Your Introduction")
characterCount = 0
wordCount = 1

for character in introString:
    characterCount = characterCount + 1
    if(character == " "):
        wordCount = wordCount + 1

print("Number of words: ")
print(wordCount)
print("Number of Characters: ")
print(characterCount)