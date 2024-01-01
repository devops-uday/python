# sample_list = [2, 20, 30, 5, 40, 80, 90, 70]
# element_to_search = 20
# for ele in sample_list:
    #   print(ele)   # To print elements in the sample_list

# for ele in sample_list:   # To search whether the element is present in the sample list and print each time element is present or not
#     if ele == element_to_search:
#         print("Element is present")
#     else:
#         print("Element is not present")

## To print even and odd nums and their sum
# even_nums = []
# odd_nums = []
# for ele in sample_list:
#     if ele % 2 == 0:
#         even_nums.append(ele)
#     else:
#         odd_nums.append(ele)

# print(even_nums, odd_nums)
# print(sum(even_nums), sum(odd_nums))

## The other way to print the sum of the even and odd elements
# sum_even = 0
# sum_odd = 0

# for ele in sample_list:
#     if ele % 2 == 0:
#         sum_even += ele
#     else:
#         sum_odd += ele

# print(sum_even, sum_odd)

# sample_str = "This is a sample string"
# for c in sample_str:
#  print(c) # can extract each character from a string

# sample_str_list = list(sample_str)
# print(sample_str_list)

# sample_str_list = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 'a', 'm', 'p', 'l', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g'] 
# sample_str = ""
# for c in sample_str_list:
#     sample_str += c
# print(sample_str) # Joining a string 

# sample_str = "".join(sample_str_list) # By join method also we can join a string
# print(sample_str)


# sample_tuple = ('a', 'b', 'c', 'd', 'e')
# for ele in sample_tuple:
#     print(ele)

# sample_tuple_list = [('a', 1), ('b', 2), ('c', 3)]
# for val1, val2 in sample_tuple_list:
#     print(val1, val2)

# d = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
# for ele in d.items():
#     print(ele)

# d = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
# for k, v in d.items():
#     print(k, v)

## Break and continue
# sample_list = [2, 20, 20, 30, 5, 40, 80, 90, 70]
# element_to_search = 20
# idx = 0
# for ele in sample_list:
#     if ele == element_to_search:
#         print("Element is found at index", idx)
#         break
#         # continue
#     idx += 1

## enumerate
# sample_list = [2, 20, 20, 30, 5, 40, 80, 90, 70]
# for idx, ele in enumerate(sample_list):
#     print(idx, ele)

## Range
# for idx in range(0, 10): # 10 is not included
#     print(idx)

# sample_list = [2, 20, 20, 30, 5, 40, 80, 90, 70]
# for idx in range(len(sample_list)):
#     print(idx, sample_list[idx])

# sample_list = [2, 20, 20, 30, 5, 40, 80, 90, 70]
# idx = 0
# while(idx < len(sample_list)):
#     print(sample_list[idx])
#     idx += 1

## zip()
# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# for ele1, ele2 in zip(list1, list2):
#     print(ele1, ele2)

sample_list = [2, 20, 20, 30, 5, 40, 80, 90, 70]
element_to_search = 20
if element_to_search not in sample_list:
    print("Element not found")
else:
    print("Element found")
