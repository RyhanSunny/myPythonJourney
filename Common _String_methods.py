# A string variable
name = "michael jackson"

# character at index 0
print(name[0])
# character at index -1: first letter backwards
print(name[-1])
# length of string
print(len(name))

# # STRING[START:END:STEP] ex: name[0:10:2]

# Slicing
print(name[0:4]) # slice from index 0 til index 4 (including 0th excluding 4th)
# Stride slicing
print(name[8:12:2]) # slice from 8th till 12th but take every 2nd character (including first letter excluding last)
# Stride values
print(name[::2]) # print only every 2nd letter from 0 till the end (including 0th and last)
# print backwards
print(name[::-1])

# Concatenating
Statement = name + " is a legend"
print(Statement)
# Tupling (Multiplying/repeating)
print(name * 3)

# escape sequence
print("This\nthen That") # new line: \n
print("This\tand that") # tab: \t
print(r"This\n\or\that") # ignore escape sequences: r

# string .is methods (boolean)
print(name.isdigit())
print(name.islower())
print(name.isalpha())


# make string all UPPER CASE
print(name.upper())

# replace
print(name.replace("j", "m"))

# find substring/character
print(name.find("son")) # if not found it will output -1

# format into title (first letter of each word capital)
print(name.title())

# COUNT: Count how many times a character sequence occurs in a string.
s = "hello world I am coding"
print(s.count('o'))

# SWAP CASE: Swap all uppercase and lowercase characters.
s = "HeLLO WORLD"
print(s.swapcase())

# JOIN: Join a list of strings into one string separated by the input string.
nums = ['dan', 'mike', 'rob']

print(' '.join(nums))
print('-'.join(nums))




