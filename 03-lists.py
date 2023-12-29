sample_list = [1, 2, 3]
sample_list = [1, 'a', 3, True]
#print(len(sample_list))

#print(sample_list[3])

sample_list = [1, 'a', 3, True, 'one', 'two', 'three', 4, 5]
#print(sample_list[::2])
#print(sample_list[1::2])

#sample_list = sample_list + [6, 7, 8]  # Here the original list remains same, since we have assigned to the same list, the list has been  altered.

#sample_list *=2
#print((sample_list))

## append(), extend()
# sample_list = [1, 2, 3]
# sample_list.append(4)  ## Appends at the end of the list and return back to the original list, where the original list is effected.
# print(sample_list)
# sample_list.extend([4,5,6]) ## Appends more than 1 element to the end of the list
# print(sample_list)
# sample_list.append([4,5,6]) ## Here the list is considered as an individual element in the list and appended
# print(sample_list)

# sample_list = [1, 2, 3, [4, 5, 6], 7, 8]
# ele = sample_list.pop(5) # Here 5th index has been popped off i.e, 8 is removed from the list
# print(ele)
# print(sample_list)

# sample_list.reverse()
# print(sample_list)

# sample_list = ['c', 'b', 'a', 'e', 'd']
# sample_list_sorted = sorted(sample_list) # Will not effect the original list
# # sample_list.sort() # will effect the original list
# print(sample_list)
# print(sample_list_sorted)

## Nesting Lists --> Lists inside a list
# sample_list = [1, 2, 3, 4, [5, 6, 7], 8, 9]
# print(sample_list[4][1]) # to extract the number inside a nested list

## To print a nested lists
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# print(list1, list2) # OR
# sample_list = [list1 , list2]
# print(sample_list)

## List unpacking  --> to extract individual elements inside a particular list
# a, b, c = [1, 2, 3]
# print(a)
# print(a, b, c)

## Swapping values
# a = 1
# b = 2
# a, b = b, a
# print(a, b)

