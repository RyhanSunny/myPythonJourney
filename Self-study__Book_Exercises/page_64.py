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
for n in oneMill:
    print(n)


