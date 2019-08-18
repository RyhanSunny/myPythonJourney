# Challenge by CoderByte
# Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
# Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

# Sample Test Cases
# Input:"hello*3"
# Output:Ifmmp*3
#
# Input:"fun times!"
# Output:gvO Ujnft!


def LetterChanges(str):
    # our new string with the modified characters
    newString = ""

    # begin by looping through each character in the string
    for char in str:

        # check if the current character is an alphabetic character
        if char.isalpha():

            # check if character is z
            if char.lower() == 'z':
                char = 'a'

            # if alphabetic character then add 1 to its ASCII value
            # by using the built-in ord function then convert back to character
            else:
                char = chr(ord(char) + 1)

        # if new character is a vowel then capitalize it
        if char in 'aeiou':
            char = char.upper()

        # add this modified character to the new string
        newString = newString + char

    return newString


print (LetterChanges("fun times!"))