

# A list in python is like an array in java
# creating List
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

