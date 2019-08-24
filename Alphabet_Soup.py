# This challenge requires you to alphabetically sort the characters in a string. We'll sort the characters using the
# built-in array sort function.


def alphabet_soup(str):

    # convert the string into a list of characters
    chars = list(str)

    # sort the list in alphabetical order
    sortedChars = sorted(chars)

    # return the newly joined string
    return "".join(sortedChars)


print('enter a random word: ')
print('Sorted alphabetically: ' + alphabet_soup(str(input().strip())))
