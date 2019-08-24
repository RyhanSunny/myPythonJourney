# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
#
list1 = []
for i in range(1, 21):
    list1 += [i]
print(list1)

# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers
# If the output is taking too long, stop it by pressing ctrl-C or by closing the output window)
#
oneMill = [i for i in range(1, 1000001)]
# for n in oneMill:
    # print(n)

# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make
# sure your list actually starts at one and ends at one million . Also, use the sum() function to see how quickly
# Python can add a million numbers

oneMill = [i for i in range(1, 1000001)]
print('min of 1 mill: ' + str(min(oneMill)))
print('max of 1 mill: ' + str(max(oneMill)))
print('sum: ' + str(sum(oneMill)))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20 .
# Use a for loop to print each number.
for i in range(1, 20, 2):
    print(i)

# 4 -7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list
for i in range(3, 30, 3):
    print(i)

# 4-8. Cubes: Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for
# loop to print out the value of each cube
cubes = [value**3 for value in range(1,10)]
print('\n')
for cube in cubes:
    print(cube)