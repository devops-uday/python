# def name_of_function():
#     num1 = 10
#     num2 = 20
#     return num1+num2

# # ans = name_of_function()
# # print(ans)
             # OR
# print(name_of_function())
            # OR
# def name_of_function(num1, num2):
#     return num1 + num2
# print(name_of_function(10, 20))

# def sum_of_values(num1=10, num2=20):
#     print(num1, num2) # num1 and num2 values are replaced by 100, 200
#     return num1+num2
# print(sum_of_values(100, 200))

## *args and **kwargs for arbitrary number of variables
# def sum_of_values(*args, **kwargs):  # Kwargs are dictionary args are tuple
#     print(args, kwargs)
#     return sum(args), sum(kwargs.values())
# print(sum_of_values(10, 20, 30, 40, 50, 60, num1 = 10, num2 = 20)) # Here 10, 20, 30, 40, 50, 60 are args and num1 and num2 are keyword args.
# print(sum_of_values(10, 20, 30, num1 = 10))
# print(sum_of_values(10, 20))

## Lambda function

# def square(num):
#     return num ** 2
# ans = square(10)
# print(ans)

#OR

# def square(num):
#     return num ** 2
# print(square(10))

#OR

# square = lambda num : num ** 2 # lambda is a inline function where we define the variable and its return value or operation
# print(square(10))

#OR

# square = lambda num : num ** 2
# ans = square(10)
# print(ans)


# sample_list = range(0, 11) # 0, 1, .... 10
# square = lambda num : num ** 2

# ans = map(square, sample_list) # Here we are using map function
# print(ans)

# for ele in ans:
#  print(ele)



# sample_list = range(0, 11)
# even = lambda x : x % 2 == 0
# ans = filter(even, sample_list)
# print(ans)
# for ele in ans:
#     print(ele)

# OR

# sample_list = range(0, 11)
# even = lambda x : x % 2 == 0
# ans = list(filter(even, sample_list)) # filter only prints true values result
# # ans = list(map(even, sample_list)) # map returns everything true and false
# print(ans)


## List comprehension --> writing in single line
sample_list = range(0,11)
# for ele in sample_list:
#     if ele % 2 == 0:
#         print(ele)
# OR
# ans = [ele for ele in sample_list if ele % 2 == 0]
ans = [ele if ele % 2 == 0 else False for ele in sample_list]
print(ans)

