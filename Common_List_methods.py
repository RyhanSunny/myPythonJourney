

# A list in python is like an array in java
# creating List
from filecmp import cmp

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7, 8]

# Accessing Values in Lists
print('list1: '+ str(list1) + '\nlist2: '+ str(list2))
print("list1[0]: ", list1[0])
print("list2[1:5] (from index 1: until 5): ", list2[1:5])

# replacing a list element:
list2[2] = 2001;
print('\nupdated list2: {}'.format(list2))

# deleting list element
del list2[2]
print('lis2 after deleting element: {}'.format(list2))

# FUNCTIONS

# append and insert
list1.append(4) # ['physics', 'chemistry', 1997, 2000, 4]
list1.insert(0, -100) # [-100, 'physics', 'chemistry', 1997, 2000]
print(list1)

# pop: Remove the last element from the list
# remove: remove a specific element from the list.
list1.pop()
print('list1 after pop: {}'.format(list1))

list1.remove(1997)
print('list1 after removing 1997: {}'.format(list1))

# get index
print(list1.index('physics'))

# Reverse the list.
list1.reverse()
print('list1 after reversing: {}'.format(list1))

# Count how many times an element appears in the list.
list3 = [1, 2, 4, 3, 2, 2, 1, 2, 3, 4, 2, 2, 2]
print('list3: {}'.format(list3))
print('2 appears on list3: {} times'.format(list3.count(2)))

# length
print(len(list3))

# Repetition
print(['Hi'* 4])

# condition and iteration
if 3 in list3:
    for i in list3:
        print(i)


# Statistics with List
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print('\n')
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehension A list comprehension combines the for loop and the creation of new elements into one line,
# and automatically appends each new element. [/expression/ /for loop to generate the numbers for the expression/]
squares = [value**2 for value in range(1,11)] # double * means square (x^2)
print(squares)
