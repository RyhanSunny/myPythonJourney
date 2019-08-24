# This challenge requires you to return the number of vowels (a, e, i, o, u) in a string. For example, if the string
# is "All cows eat grass" then your program should return the integer 5. The first program is a basic loop that keeps
# track of the vowels it encounters.

string = str(input('Enter a sentence: ').strip())

vowels = {i:0 for i in 'aeiou'}
for char in string.lower():
    if char in vowels:
        vowels[char] += 1


